#!/bin/bash

######
#Clears Chrome and Safari Cache for Inside Adobe issues
#by Phillip White
#I accept no responsibility if this script destroys your computer, saved progress, or your life
######


u=$Username

#This is by no means a comprehensive clearing of the web browser cache but should fix the issue that inside adobe gets stuck on
echo "Clearing Chrome Cache..."

rm -rf /Users/$u/Library/Caches/Google/Chrome/Default/Cache/

echo "Clearing Safari Cache..."

rm -rf /Users/$u/Library/Containers/com.apple.Safari/Data/Library/Caches/*

echo "Opening a Inside Adobe to test..."

open https://inside.corp.adobe.com/
