(this takes roughly 4~5min)

Hello everyone, today I'm going to present my cvpr paper, enhancing adversarial
robustness for deep metric learning.

Given a set of data points, deep metric learning aims to learn a mapping
function to project the data onto a embedding space, where similar data
points are close to each other, while disimilar data points are far away from
each other. It has lots of important applications.

However, recent studies reveal that by adding a small and imperceptible
adversarial perturbation to the image, the deep metric learning model will
produce incorrect results.

Considering the security implications, it is important to improve the
adversarial robustness. However, existing defense methods still suffer from low
training efficiency and notable performance drop on benign examples.

Now, we rethink about the problem. Assume there are two extreme methods.  The
weakest one is regular training, while the strongest one is the madry defense.
Although madry defense is promising for classification, it results in model
collapse in deep metric learning. Based on this, our insight is to find an
intermediate point between the two extremes.

So, we propose hardness manipulation, to perturb a given image triplet and
increase its hardness level to a specified destination hardness level.  The
resulting adversarial examples are used for training.

Hardness Manipulation is efficient, because it has the same gradient as
directly maximizing the loss. But differently, it stops at a specified
desination hardness.

That means the flexibility stems from destination hardness HD.  When it equals
the original source hardness HS, it degenerates into regular training. When HD
equals 2, it degenerates into the madry defense.  So, we can specify any value
between HS and 2.

So, what exact hardness value should be specified? We start from using the
existing triplet sampling strategies.  After searching by brute force, we find
two promising combinations, where the best one is to perturb softhard triplets
into semihard triplets.

We then conduct experiments with the good combinations. We will skip the bulky
table and directly see curves. The left plot shows the efficiency in obtaining
a high robustness under a low training cost. The right plot indicates the
performance drop on benign examples. The red curve is generally performing very
well without any tuning, so we will continue from this new baseline.

As aforementioned, we find the adversarial examples not strong enough in the
late phase of training, and the adversarial examples may be too strong in the
early phase of training. To simultaneously address them, we propose linear
gragual adversary, which is used as a dynamic destination hardness.

After adding this, the red curve becomes the pink curve.  The resulting method
is as efficient in gaining robustness as the red curve, but it can achieve a
better performance on benign examples.

Next, we also note that by benign triplet plus adversarial triplet is
a sextuplet. In this case, enforcing intra-class structure is possible.
Considering there are attacks aiming to change item ranking within the same
class, which is neglected by previous defense methods, we design
a corresponding loss term.

Then the pink curve becomes yet another red curve with improved model robustness.

In a word, If we combine the improvements altogether, we can see our proposed
method, namely the red curve, overwhelmingly outperforms the previous state of
the art method.

And we have the same conclusions on the other commonly used deep metric learning
datasets.

Ok. Adversarial defense is important for deep metric learning. In this paper,
we propose Hardness manipulation for flexible adversarial training,
which overwhelmingly outperforms the state-of-the-art defense when combined
with linear gradual adversary and Intra-class structure loss.

That's all, thank you for listening.
