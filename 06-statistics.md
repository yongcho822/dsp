# Learn Statistics

Read Allen Downey's [Think Stats (second edition)](http://greenteapress.com/thinkstats2/) and [Think Bayes](http://greenteapress.com/thinkbayes/) for getting up to speed with core ideas in statistics and how to approach them programmatically. Both books are completely available online, or you can buy physical copies if you would like.

[<img src="img/think_stats.jpg" title="Think Stats" width="250" style="float: left;" />](http://greenteapress.com/thinkstats2/)
[<img src="img/think_bayes.png" title="Think Bayes" style="float: left"; />](http://greenteapress.com/thinkbayes/)

Some people enjoy video content such as Khan Academy's [Probability and Statistics](https://www.khanacademy.org/math/probability) or the much longer and more in-depth Harvard [Statistics 110](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo). You might also be interested in the book [Statistics Done Wrong](http://www.statisticsdonewrong.com/) or a very short [overview](http://schoolofdata.org/handbook/courses/the-math-you-need-to-start/) from School of Data.


Complete the following exercises. They come from Think Stats, and some can be solved using code provided with the book. The preface of Think Stats [explains](http://greenteapress.com/thinkstats2/html/thinkstats2001.html#toc2) how to use the code.

Communicate the problem, how you solved it, and the solution, within each of the following [markdown](https://guides.github.com/features/mastering-markdown/) files. (You can include code blocks and images within markdown.)

1. [Think Stats Chapter 2 Exercise 4](statistics/2-4-cohens_d.md) (Cohen's d)
2. [Think Stats Chapter 3 Exercise 1](statistics/3-1-actual_biased.md) (actual vs. biased)
3. [Think Stats Chapter 4 Exercise 2](statistics/4-2-random_dist.md) (a random distribution)
4. [Think Stats Chapter 5 Exercise 1](statistics/5-1-blue_men.md) (blue men)
5. [Think Stats Chapter 6 Exercise 1](statistics/6-1-household_income.md) (household income)
6. [Think Stats Chapter 7 Exercise 1](statistics/7-1-weight_vs_age.md) (weight vs. age)
7. [Think Stats Chapter 8 Exercise 2](statistics/8-2-sampling_dist.md) (sampling distribution)
8. [Think Stats Chapter 8 Exercise 3](statistics/8-3-scoring.md) (scoring)
9. [Think Stats Chapter 9 Exercise 2](statistics/9-2-resampling.md) (resampling)


---

Elvis Presley had a twin brother who died at birth.  What is the probability that Elvis was an identical twin?

Alright, if we know that Elvis had a twin brother, our two possibilities/hypotheses are:

1. Elvis was an identical twin

2. Elvis was a fraternal twin 

According to http://www.babycentre.co.uk/a539828/how-common-are-twins', identical twins constitute about 1/3rd of twins. 

So p(1) = 0.33, p(2) = 0.66

We know that this twin was a male and identical twins are the same gender.

p(m|1) = 1

p(m|2) = 0.5

We want to find p(1|m).

Using Baye's Theorem, p(1|m) = (p(1)*p(m|1))/p(m) = (0.33)*(1)/0.5 = 0.66.

If identical twins are a third of all twins, there's a 2/3 chance that Elvis was an identical twin.

---


---

How do frequentist and Bayesian statistics compare?

I'm not completely sure I've fully gasped an understanding of it, but this is what I know thus far:

In Bayesian stats, everything is assigned probabilities, and things are computed mathematically/logically that way. Unknown quantities are treated probabilistically, prior information is factored in, and the state of the world can be constantly updated.

In Frequentist stats, things are more set in stone and probabilitiy is more-so looked at as long-term 'frequency'. Probability statements can ony made about samples.

---
