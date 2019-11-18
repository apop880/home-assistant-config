import appdaemon.plugins.hass.hassapi as hass
from emoji import emojize
import globals

#
# Good morning. Gentle wakeup triggered by Alex's alarm.
#
#

class GoodMorning(hass.Hass):

	def initialize(self):
		self.loop_timer = None
		self.awake_listener = None
		self.cancel_wakeup_listener = None
		self.listen_event(self.good_morning, "good_morning")
	
	def good_morning(self, event_name, data, kwargs):
		self.color_temp = 2200
		self.brightness = 10
		self.turn_off("input_boolean.night_mode")
		if self.get_state("input_boolean.alex_basement") == "off":
			keyboard = [[("I'm Awake", "/awake"),("Cancel Wakeup", "/cancel_wakeup")]]
			self.call_service("telegram_bot/send_message", message = emojize(":sunny: Wake up!", use_aliases=True), target = globals.alex, inline_keyboard=keyboard)
			self.turn_on("light.alex_lamp", kelvin=self.color_temp, brightness_pct=self.brightness)
			self.awake_listener = self.listen_event(self.awake, "telegram_callback", data="/awake")
			self.cancel_wakeup_listener = self.listen_event(self.cancel_wakeup, "telegram_callback", data="/cancel_wakeup")
			if self.sun_down():
				self.turn_on("light.kitchen_sink", brightness_pct=40)
			self.turn_on("light.alex_lamp", kelvin=3500, brightness_pct=70, transition=60*30)
			self.run_in(self.normalize, 60*40)
		elif self.sun_down():
			self.turn_on("light.kitchen_sink", brightness_pct=40)
			self.turn_on("light.stairs", brightness_pct=40)
	
	def awake(self, event_name, data, kwargs):
		if self.awake_listener != None:
			self.cancel_listen_event(self.awake_listener)
		if self.cancel_wakeup_listener != None:
			self.cancel_listen_event(self.cancel_wakeup_listener)
		self.turn_on("light.alex_lamp", kelvin=2700, brightness_pct=50)
		self.call_service("telegram_bot/edit_replymarkup", chat_id=globals.alex, message_id="last", inline_keyboard=None)
	
	def cancel_wakeup(self, event_name, data, kwargs):
		if self.awake_listener != None:
			self.cancel_listen_event(self.awake_listener)
		if self.cancel_wakeup_listener != None:
			self.cancel_listen_event(self.cancel_wakeup_listener)
		self.turn_on("light.alex_lamp", kelvin=2700, brightness_pct=20)
		self.turn_off("light.alex_lamp")
		self.call_service("telegram_bot/edit_replymarkup", chat_id=globals.alex, message_id="last", inline_keyboard=None)
	
	def normalize(self, kwargs):
		if self.get_state("light.alex_lamp") == "on":
			self.turn_on("light.alex_lamp", kelvin=2700, brightness_pct=40)
		self.call_service("telegram_bot/edit_replymarkup", chat_id=globals.alex, message_id="last", inline_keyboard=None)