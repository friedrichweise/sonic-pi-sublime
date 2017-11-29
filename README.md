# Sonic Pi Sublime Text 3 Plugin

My attempt is to write a Sublime Text 3 Plugin that allows writing Sonic Pi Code in Sublime. 

<img src="screen.png" alt="screenshot"/>

## Getting Started

Under the menu entry `Tools` you are able to select 4 actions in the corresponding `Sonic Pi` submenu:
* **Start Live Mode**: With this mode enabled saving a file in Sublime sends it to the Sonic Pi Server
* **Stop Live Mode**: Disables the mode
* **Play Current File**: Sends the file in the current tab to the Sonic Pi Server
* **Stop All Jobs**: Stops all threads on the Sonic Pi Server. Also triggered by **Stop Live Mode**

Key bindings can be modified in `Default.sublime-keymap`.

## Compability

*Feel free to contribute to this table:*

| OS Version | Sublime Text Version | Sonic Pi Version | Tested |
|:-:|:-:|:-:|:-:|
| macOS 10.13 | 3.0 | 3.0.1 | ✅ |


## Features
Please use the Github Issues for Feature requests-

* autocompletion
* show logging information from server
* visualize Live-Mode with green dot
