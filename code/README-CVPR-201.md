Code implmentation for CVPR2022 Submission 201
===

Brief usage instructions:

1. download and prepare datasets as described in `README-upstream.md`.

2. generate python configurations for the models by running `bash tools/autogen.bash`.

3. train our defensive models on CUB, CARS, SOP datasets:

```
Command Table
CUB  | HM[S,g_LGA]     | python3 bin/train.py -C cub:rres18ghmetsm:ptripletN
CARS | HM[S,g_LGA]     | python3 bin/train.py -C cars:rres18ghmetsm:ptripletN
CUB  | HM[S,g_LGA]     | python3 bin/train.py -C sop:rres18ghmetsm:ptripletN
CUB  | HM[S,g_LGA]&ICS | python3 bin/train.py -C cub:rres18ghmetsmi:ptripletN
CARS | HM[S,g_LGA]&ICS | python3 bin/train.py -C cars:rres18ghmetsmi:ptripletN
CUB  | HM[S,g_LGA]&ICS | python3 bin/train.py -C sop:rres18ghmetsmi:ptripletN
```

4. evaluate these models following the description in `README-upstream.md`

Acknowledgement:

Our code is based on the public code of the following paper:
"Adversarial Attack and Defense in Deep Ranking" ArXiv: 2106.03614
