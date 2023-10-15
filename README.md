# EnergiBridge Experiements

## Setup

1. Download the latest release of EnergiBridge: https://github.com/tdurieux/EnergiBridge/releases and copy the binary to the energibridge folder.
If you are on Windows, you also have to setup the driver. The instructions are in the EnergiBridge/readme.md.

2. Download the llama model from https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/blob/main/llama-2-7b-chat.Q4_0.gguf and put it in workloads/llama/models/

### Linux & Mac
```
git submodule init
git submodule update
cd workloads/llama/llama.cpp
```

### Windows
Downloads the release of llama.cpp: 
https://github.com/ggerganov/llama.cpp/releases


## Results