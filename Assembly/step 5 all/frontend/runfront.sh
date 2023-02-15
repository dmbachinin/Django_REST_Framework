#!/bin/bash
port=3000
fuser -k $port/tcp
npm start