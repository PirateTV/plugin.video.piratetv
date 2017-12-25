import xbmcaddon, util

addon = xbmcaddon.Addon('plugin.video.piratetv')

util.playMedia(addon.getAddonInfo('name'), addon.getAddonInfo('icon'), 
               'rtmp://stream.piratetv.eu/live/piratetv')
