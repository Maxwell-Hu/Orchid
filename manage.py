#!/usr/bin/env python

import os
from app import create_app
from app.config import configs

app = create_app(configs[os.getenv('FLASK_ENV') or 'dev'])
