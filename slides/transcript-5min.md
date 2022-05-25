(this takes roughly 4~5min)

Hello everyone, today I'm going to present my cvpr paper, enhancing adversarial
robustness for deep metric learning.

Given a set of data points, deep metric learning aims to learn a mapping
function phi to project the data onto a embedding space.  In the embedding
space, similar data points are close to each other, while disimilar data points
are far away from each other.  It has lots of applications, including image
retrieval, face recognition, and cross-modal retrieval.

However, recent studies reveal the adversarial vulnerability of deep neural
networks. Namely, by adding a small and imperceptible adversarial perturbation
to the image, the deep metric learning model will produce incurrect results.

Considering the security implications of the attacks, it is important to defend
against the attacks and improve the adversarial robustness. But this topic is
not yet sufficiently explored. There are some existing defense methods based on
adversarial training, but they suffer from low training efficiency and notable
performance drop on benign examples.

In this project, we rethink about the defense problem. Assume there are two
extreme points. The weakest point is regular training, while the strongest is
the direct adaptation of madry defense. Although madry defense is promising for
classification, it results in model collapse in deep metric learning. Based on
this, our insight is to simply and efficiently find an intermediate point
between the two extremes, that can lead to a robust model without incurring
model collapse.

So, we define the hardness, an internal part in triplet loss of images.  Then,
we propose hardness manipulation, to perturb a given image triplet to increase
its hardness level to a specified destination hardness level.  And the
resulting adversarial examples are used for training.

Hardness Manipulation is efficient, because the sign of its gradients with
respect to the perturbation is the same as that for directly maximizing the
hardness.  So, hardness manipulation can be interpreted as a direct maximizaion
process which stops at the specified desination.

That means the flexibility of hardness manipulation stems from destination
hardness HD.  When it equals the original hardness HS, it degenerates into
regular training. When HD equals 2, it degenerates into the madry defense. So,
we can specify any value between HS and 2.

So, what hardness value should be specified? We start from using the hardness
of benign examples sampled with different strategies, because they do not lead
to model collapse in regular training.  After searching by brute force, we find
two promising combinations. We can purturb random triplets into
semihard triplets, or perturb softhard triplets into semihard triplets.

We conduct complete experiment with the two promising combinations. We will
skip the bulky table and directly see curves. The left subplot indicates the
efficiency of a method, namely to obtain a high robustness under a fixed
training cost. The right subplot indicates the performance drop on benign
examples as a trade-off for robustness. The red curve is generally performing
very well without any tuning in details, so we will continue from this new
baseline.

As aforementioned, we find the adversarial examples not strong enough in the
late phase of training. Meanwhile, the adversarial examples may be too strong
in the early phase of training. To simultaneously address these issues, we
propose linear gragual adversary, which is used as a dynamic destination
hardness.

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
Hardness manipulation is proposed for flexible adversarial training.
Linear gradual adversary is proposed to balance the training objectivess.
Intra-class structure loss is proposed to further improve model robustness.
And our method overwhelmingly outperforms the sota.

That's all, thank you for listening.
