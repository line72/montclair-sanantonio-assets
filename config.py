# -*- mode: python -*-

import transmogrifier

CONFIG = transmogrifier.Config(
    build_dir = './build',
    repo = 'sanantonio',
    package_name = 'montclair-sanantonio',
    name = 'Go San Antonio',
    description = 'Real Time Tracking of the Buses for San Antonio, TX',
    url = 'https://sanantonio.gotransitapp.com',
    logo_svg = 'assets/logo.svg',
    montclair_config = transmogrifier.MontclairConfig(
        version = '1.7.5',
        revision = 1,
        title = 'Go San Antonio',
        first_run_text = "Welcome to San Antonio, TX's Real Time Bus Tracker.<br /><br />Please select one or more routes to begin!",
        configuration_js_file = 'assets/Configuration.js'
    ),
    ios_config = transmogrifier.MontclairiOSConfig(
        version = '2.0.5',
        revision = 1,
        app_id = 'com.gotransitapp.sanantonio',
        app_store_id = 'REPLACE_ME',
        app_store_url = 'https://apps.apple.com/us/app/REPLACE_ME'
    ),
    android_config = transmogrifier.MontclairAndroidConfig(
        version = '1.0.2',
        revision = 1,
        app_id = 'com.gotransitapp.sanantonio',
        play_store_url = 'https://play.google.com/store/apps/details?id=com.gotransitapp.sanantonio'
    )
)
