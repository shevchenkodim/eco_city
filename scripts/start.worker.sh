#!/bin/sh
celery -A core worker -l info -P solo