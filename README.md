Robust Deep Metric Learning (RobDML)
===

**Title:** Enhancing Adversarial Robustness for Deep Metric Learning  
**Authors:** Mo Zhou, Vishal Patel  
**Conference:** CVPR, 2022  
**Preprint:** https://arxiv.org/abs/2203.01439  
**Code:** https://github.com/cdluminate/robrank  

## Brief usage instructions:

Our code is based on the public code of the following paper:
["Adversarial Attack and Defense in Deep Ranking" arXiv: 2106.03614](https://github.com/cdluminate/robrank).

1. download and prepare datasets as described in [`README.md`](https://github.com/cdluminate/robrank/blob/main/README.md).

2. generate python configurations for the models by running `bash tools/autogen.bash`.

3. train our defensive models on CUB, CARS, SOP datasets:

```
Command Table
CUB  | HM[S,g_LGA]     | python3 bin/train.py -C cub:rres18ghmetsm:ptripletN
CARS | HM[S,g_LGA]     | python3 bin/train.py -C cars:rres18ghmetsm:ptripletN
SOP  | HM[S,g_LGA]     | python3 bin/train.py -C sop:rres18ghmetsm:ptripletN
CUB  | HM[S,g_LGA]&ICS | python3 bin/train.py -C cub:rres18ghmetsmi:ptripletN
CARS | HM[S,g_LGA]&ICS | python3 bin/train.py -C cars:rres18ghmetsmi:ptripletN
SOP  | HM[S,g_LGA]&ICS | python3 bin/train.py -C sop:rres18ghmetsmi:ptripletN
```

4. evaluate these models following the description in [`README.md`](https://github.com/cdluminate/robrank/blob/main/README.md)

## License

Apache-2.0
