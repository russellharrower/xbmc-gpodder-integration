"""
    Document   : start.py
    Package    : GPodder Integration to XBMC
    Author     : Ashley Kitson
    Copyright  : 2010, Ashley Kitson, UK
    License    : Gnu General Public License - see LICENSE.TXT
    Description: Main program script for package
"""
"""
This file is part of "The GPodder Integration to XBMC"

    "The GPodder Integration to XBMC" is free software: you can redistribute
    it and/or modify it under the terms of the GNU General Public License as
    published by the Free Software Foundation, either version 3 of the License,
    or (at your option) any later version.

    "The GPodder Integration to XBMC" is distributed in the hope that it will
    be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with "The GPodder Integration to XBMC".
    If not, see <http://www.gnu.org/licenses/>.

"""
#
# Step 1 - load in core support and setup the environment
#
import os
import sys
import xbmcplugin

# magic; id of this plugin's instance - cast to integer
_thisPlugin = int(sys.argv[1])

#addon id - name of addon directory
#TODO XBMC Trac 10171 - why do we need to do this - should be able to get
# id from current running instance of plugin
_id='plugin.audio.gpodder-xbmc'

#set our library path
sys.path.append (xbmc.translatePath( os.path.join( os.getcwd(), 'resources', 'lib' ) ))

#import our worker classes from our module
import xbmc_gpodder as worker

#
# Step 2 - instantiate the support classes
#
housekeeper = worker.housekeeper(_thisPlugin, _id)
creator = worker.creator(_thisPlugin, _id)
sender = worker.sender(_thisPlugin)

#
# Step 3 - run the program
#
housekeeper.start()
sender.send(creator.get())
xbmcplugin.endOfDirectory(_thisPlugin)
housekeeper.end()
