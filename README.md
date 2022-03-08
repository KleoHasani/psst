<div id="header" align="center">
  <img src="https://media.giphy.com/media/26xBLq0QJdxy57CV2/giphy.gif" width="200"/>
</div>

---

# PSST

## Description

Port Super Scanner Tool.

---

## Table of Contents

- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Installation](#installation)
    - [Clone](#clone)
    - [VENV](#venv)
    - [Install](#install)
    - [Start](#start)
    - [Stop](#stop)
- [Build](#build)
- [Usage](#usage)
- [Test](#test)
- [Create Executable](#create-executable)
- [Run Executable](#run-executable)

---

## Getting Started

- ## Requirements

  - [x] Python3 v3.10
  - [x] Poetry v1.1

- ## Installation

  - ### Clone

    ```shell
    git clone https://github.com/KleoHasani/psst.git
    ```
  - #### VENV

    ```shell
    poetry shell
    ```

    **Set your shell to use the venv paths for Python by activating the virtual environment.**
    - Windows

      ```shell
      .\.venv\Scripts\activate
      ```

    - *nix
      ```shell
      source .venv/bin/activate
      ```

  - ### Install

  ```python3
  poetry install
  ```

- ### Start
  ```
  python3 psst/main.py
  ```
  - ### Stop

    **Disable venv for the project.**

    ```shell
    deactivate
    ```

---

## Build

```shell

```

---

## Usage

---

## Test

```shell
poetry run pytest
```

| File         | Test             | Description | Status   |
| :----------- | :--------------- | :---------- | :------- |
| test_true.py | test_always_true | Mock test.  | &#10003; |