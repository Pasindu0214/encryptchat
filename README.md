# Chat Application Setup Guide

## Step 1: Ensure Pip is Installed

1. Open the terminal.
2. Execute the command: `py -m ensurepip --upgrade`. This ensures that Pip, the Python package installer, is installed and up to date.

## Step 2: Install RSA Library

After ensuring Pip is installed, execute the following command to install the RSA library for Python, which is necessary for cryptographic operations in your chat application:

Execute the command: `pip install rsa`.

## Step 3: Configuration for Local Use

By default, the chat app will run on the same device without requiring manual IP configuration. No changes are needed if running on the same device; local IP addresses will be automatically used.

## Step 4: Configuration for Public IP (Optional)

If you intend to use the chat app with a public IP address (to communicate over the internet), follow these steps:

1. Replace `local_ip` with your public IP address in your Python code (specifically, on lines 26 and 37 where IP configuration is mentioned).
2. Ensure port forwarding is set up on your router for port 9999 to direct incoming traffic to the device running the chat app.
