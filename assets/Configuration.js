/* -*- Mode: rjsx -*- */

/*******************************************
 * Copyright (2018)
 *  Marcus Dillavou <line72@line72.net>
 *  http://line72.net
 *
 * Montclair:
 *  https://github.com/line72/montclair
 *  https://montclair.line72.net
 *
 * Licensed Under the GPLv3
 *******************************************/

import GTFSRTParser from './GTFSRTParser';

class Configuration {
    constructor() {
        // San Antonio, TX
        this.center = [29.4246002, -98.4951405];

        this.agencies = [
            {
                name: 'Routes',
                parser: new GTFSRTParser('montclair', '/sanantonio-gtfs.zip',
                                         'https://sanantonio.gotransitapp.com/api/no.php/vehicle/vehiclepositions.pb',
                                         'https://sanantonio.gotransitapp.com/api/no.php/tripupdate/tripupdates.pb')
            }
        ];
    }
}

export default Configuration;
