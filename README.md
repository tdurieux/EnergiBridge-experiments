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

Download cpu stress test https://web.archive.org/web/20070119115200/https://download.microsoft.com/download/8/e/c/8ec3a7d8-05b4-440a-a71e-ca3ee25fe057/rktools.exe

### Mac
Install `brew install sysbench`

## Results

The raw results of our experiments are available in the `/results` folder.
The results are devided by platform, by date and by workload.
The results can also by vizualized inside the Jupiter notebook: `analysis.ipynb`.

## Worlkoads

The replication package currently support 5 workloads:

1. Chrome
2. Firefox
3. IDLE
4. llama
5. CPU warmup