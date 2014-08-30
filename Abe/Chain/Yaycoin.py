# Copyright(C) 2014 by Abe developers.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.

from .Sha256Chain import Sha256Chain

class Yaycoin(Sha256Chain):
    def __init__(chain, **kwargs):
        chain.name = 'yaycoin'
        chain.code3 = 'YAY'
        chain.address_version = "\x4e"
        chain.magic = "\xfb\xc0\xb6\xdb"
        Sha256Chain.__init__(chain, **kwargs)

    datadir_conf_file_name = "yaycoin.conf"
    datadir_rpcport = 8383