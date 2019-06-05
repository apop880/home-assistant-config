# My Home Assistant Config

This is very much still a work in progress, but I wanted to share my
configuration as a few people have asked for it. So far, I just have my
configuration.yaml file, my Lovelace configuration, and a few other files. I
will be putting my AppDaemon scripts out here soon but I'm finishing up some
clean-up with those. In the meantime, I do have a couple of scripts currently
posted [in a separate repo.](https://github.com/apop880/AppDaemon)

There are a couple of known issues or things to note with my Lovelace
configuration:
* I am using YAML mode with includes. `ui-lovelace.yaml` is my root Lovelace file,
  and my individual views are inside the `lovelace` folder. If you wish to use
  this config as a baseline, it will be easiest if you start in YAML mode.
  Otherwise, you can certainly use bits and pieces in Storage mode. I started
  off in Storage mode before my configuration increased in complexity and I
  migrated to YAML mode.
* I also make heavy use of anchors in my configuration right now. I'm looking at
  using the decluttering-card and template features added to the button-card
  instead, but for now, the anchors have been the route I've taken. It's a big
  time saver for reusing sections, but it can make it a little more difficult to
  piece together what the config is doing. I'd recommend starting with [this
  link](https://github.com/thomasloven/hass-config/wiki/Misc-tricks) and [this
  link](https://community.home-assistant.io/t/solved-using-yaml-anchors-saves-time-and-space/112416)
  for an introduction to anchors.
  
* The configuration is highly mobile-focused
  right now. I plan to add some
  PC-centric views down the line, but mobile is definitely the priority.
* Most of the views are currently geared towards portrait orientation use. A few
  of them look alright in landscape, but I haven't put a great deal of effort
  into that yet. My focus is definitely on portrait view, scaled to my phone
  screen (LG V30).
* I still have some minor cleanup to do in some of the code and will continue to
  push commits as I make updates. But the Lovelace configuration is in a fully
  usable, pretty finished state, so I wanted to get something out there for
  people to look at and possibly take inspiration from.
* Sometimes, the conditional views don't always render the first time. I think
  this may be because I have custom button cards inside of stacks, inside of
  conditionals. So, I've noticed occasions where the conditional card won't show
  up. Most often, this seems to occur if the conditional changes to true, and
  you go back into Home Assistant and it has to reconnect. This is generally
  fixed by a refresh of the page.

## Screenshots
More screenshots and information on what is happening on each page will be posted soon.

<table><tr><td>
<img src="https://raw.githubusercontent.com/apop880/home-assistant-config/master/lovelace/screenshots/chromecast_remote.jpg" width=200>
<img src="https://raw.githubusercontent.com/apop880/home-assistant-config/master/lovelace/screenshots/xbox_remote.jpg" width=200>
<img src="https://raw.githubusercontent.com/apop880/home-assistant-config/master/lovelace/screenshots/tvs.jpg" width=200></td></tr><tr><td>
<img src="https://raw.githubusercontent.com/apop880/home-assistant-config/master/lovelace/screenshots/lights.jpg" width=200>
<img src="https://raw.githubusercontent.com/apop880/home-assistant-config/master/lovelace/screenshots/climate.jpg" width=200>
<img src="https://raw.githubusercontent.com/apop880/home-assistant-config/master/lovelace/screenshots/system.jpg" width=200></td></tr></table>