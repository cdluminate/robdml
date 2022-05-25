(this takes roughly 7 min ~ 10 min)

Hello everyone, my name is Mo. Today I'm going to present my project, enhancing
adversarial robustness for deep metric learning.

Given a set of data points, deep metric learning aims to learn a mapping
function phi to project the data onto a embedding space.  In the embedding
space, similar data points are close to each other, while disimilar data points
are far away from each other.  So, by computing the distance between the
embedding vectors, we will know how similar the two chosen data points are.

Deep metric learning has lots of applications, including image retrieval, face
recognition, cross-modal retrieval, as well as self-supervised learning.

The succuess of deep metric learning is built upon deep neural networks.
However, recent studies reveal the adversarial vulnerability of deep neural
networks. Namely, by adding a small and imperceptible adversarial perturbation
to the image, the deep neural networks will incorrectly classify the perturbed
image. The same issue also exists on deep metric learning models.

Considering the security implications of the attacks, it is important to defend
against the attacks and improve the adversarial robustness. But this topic is
not yet sufficiently explored. There are some existing defense methods based on
adversarial training, but they suffer from high training cost and performance
drop on unperturbed examples.

In this project, we rethink about the defense problem. Assume there are two
points. The first point is regular training, it does not lead to a robust
model.  The other is the direct adaptation of madry defense. it is the best
defense in the classification problem, but it will result in model collapse in
deep metric learning. so it is not feasible. Based on this, our insight is to
simply find an intermediate point between the two methods, that can lead to a
robust model without incurring model collapse.

So, we define the hardness of a triplet of images as H. It is an internal part
of the standard triplet loss function. Then, we propose a flexible tool for
creating adversarial examples for adversarial training. Given a triplet, we
define its hardness as source hardness HS. Then we specify a destination
hardness HD, and find adversarial perturbations that can increase HS towards
HD. The resulting adversarial examples are used for training.

The proposed method has an important characteristics. The sign of its gradients
with respect to the perturbation is the same as that for directly maximizing
HS. So, hardness manipulation can be interpreted as a direct maximizaion
process which stops at the specified desination hardness instead of pushing
it towards the theoretical upperbound.

The flexibility of HM stems from HD. It can be a constant, the hardness of
another benign triplet, or a pseudo-hardness function. When HD equals HS, it
degenerates into regular training. When HD equals to 2, it degenerates into the
direct adaptation of madry defense. So, we can specify any value between HS and
2.

So, what hardness value should be specified? We start from using the hardness
of existing benign triplets, because they do not lead to model collapse.  After
searching by brute force, we find two promising combinations. Actually, there
are many intriguing interpretations in the right table, but I will not dive
into the details.

We conduct complete experiment with the two promising combinations. Don't
worry, we dont look at the bulky table. The left subplot indicates the
efficiency of a method, namely to gain a high robustness under a fixed training
cost. The right subplot indicates the performance drop on benign examples as a
trade-off for robustness. The red line is good at both aspects, so let's
continue with it.

With deeper analysis, we find the adversarial examples not strong enough in the
late phase of training. Apart from that, the adversarial examples may be too
strong in the early phase of training when the embedding space is not in shape.
To simultaneously address these issues, we propose linear gragual adversary,
which can be used as destination hardness.

Now let's look at the pink line. It is as efficient in gaining robustness as
the red line, but it can achieve a better performance on benign examples.

Next, we note that by combining the benign triplet and adversarial triplet, we
obtain a sextuplet. In this case, enforcing intra-class structure is possible.
Considering there are attacks aiming to change item ranking within the same
class, and this has been neglected by previous defense methods, we design
an intra-class structure loss term.

It can further improve the model robustness.

If we combine all the improvements together, we can see the proposed method,
namely the red line, overwhelmingly outperforms the previous state of the art
method.

We have conducted experiments on other datasets, and the conclusion is the
same.

Ok. Adversarial defense is important for deep metric learning. In this project,
Hardness manipulation is proposed as a flexible tool for adversarial training.
Linear gradual adversary is proposed to balance the training objectivess.
Intra-class structure loss is proposed to further improve model robustness.

Given the limited time, we cannot dive into technical details. What I presented
is the high level ideas underlying this work.  the corresponding paper will be
available on arxiv soon.

That's all, thank you for listening.
