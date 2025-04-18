# Pi4Kids Educational Game

A simple Raspberry Pi-based educational game for advanced kindergarteners.

## Features

- Voice-based question and feedback
- Supports multiple subjects
- Simple JSON-based question bank
- Input via USB keyboard

## Usage

1. Install `espeak`:
    ```bash
    sudo apt-get install espeak
    ```

2. Run the game:
    ```bash
    python3 main.py
    ```

## Folder Structure

- `questions/`: JSON question banks for each subject
- `utils/`: Helper utilities for TTS
