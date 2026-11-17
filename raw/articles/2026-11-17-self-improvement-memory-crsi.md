# Self-Improvement Memory Enables Continual Recursive Self-Improvement

> Origin: https://t.co/VvUfmVFC3H (redirects to https://arxiv.org/abs/2611.18856)
> Received via Telegram: 2026-11-17T17:29:28+00:00
> Authors: Xin Yu, Fei Xia, Jiaqi Pan, Youbao Tang, Chengzhi Liu, Adams Yu, Sicong Jiang, Yanfei Chen, Lingzhou Xue, Ting Yu (Google Cloud AI, Google DeepMind, Penn State)
> arXiv:2611.18856v1 [cs.LG], 13 Nov 2026
> Note: text extracted automatically from the PDF (main body, pages 1–10; references and appendices omitted). Figure/table layout may be garbled.

## Paper text

2026-11-13

Self-Improvement Memory Enables Continual
Recursive Self-Improvement
Xin Yu1,4,* , Fei Xia1 , Jiaqi Pan1 , Youbao Tang1 , Chengzhi Liu1 , Adams Yu2 , Sicong Jiang2 , Yanfei Chen3 ,
Lingzhou Xue4 and Ting Yu1
1 Google Cloud AI
2 Google DeepMind
3 Google Cloud AI Research
4 The Pennsylvania State University

Harness optimization is often studied with a fixed
policy model and benchmark. When either changes,
the optimizer must decide which parts of an
evolved harness to reuse or revise, but the harness
alone may not explain why earlier edits were made
or how they performed. In this work, we study Continual Recursive Self-Improvement (CRSI), a setting for continuing existing harness-optimization
methods across compatible benchmarks or policy
models. We propose Self-Improvement Memory
(SIM) for the harness optimizer, rather than the
task-solving policy. SIM groups edits by recurring harness problem and records their rationale,
predicted and observed outcomes, and evaluation
context. New attempts extend this history as optimization continues. In our experiments across
four domains, SIM achieves higher final scores
than harness-only and root-cause-only continuation in cross-dataset and pairwise cross-model comparisons. Across ten independent source runs in
coding, paired continuations with SIM improve final scores by an average of 2.36 points over harnessonly continuation (p = 0.003).

Keywords: Recursive self-improvement, agent harnesses, continual learning

1. Introduction
An LLM agent depends on both its policy model
and the harness that manages context, tools,
and execution. Improving the harness can raise
performance without updating model weights,
* This work was done while Xin Yu was an intern at

Google.

Corresponding author(s): xinyulucas@google.com
© 2026 Google. All rights reserved

Direct transfer

CRSI with SIM

Source RSI

Source RSI

HS

HS

Evolved harness

Evaluate target

SIM

+

Evolved harness + SIM

Target RSI
Update harness + SIM

CRSI TARGET SETTINGS

Data
Policy fixed

Models
Benchmark /
split fixed

Held-out score

arXiv:2611.18856v1 [cs.LG] 13 Nov 2026

{xinyulucas, feixia, jiaqip, tangyoubao, chengzhiliu, adamsyuwei, jiangsicong, yanfeichen, yuti}@google.com,
lzxue@psu.edu

85

Coding · Text classification
Workspace · Engineering
Families · Generations
Shared harness across models

(a) Transfer and continued improvement
With SIM 84.75

75
68.41
65
Before RSI

Without SIM 73.42
After RSI

(b) Cross-model workspace continuation

Figure 1 | Continual improvement beyond direct
transfer. (a) CRSI carries the evolved harness and
SIM into target RSI across data or models. SIM
guides reuse and revision. (b) Both conditions continue RSI from the same Opus-evolved harness on
Gemini’s workspace tasks; arrows join measured
endpoints with matched rounds and candidates.

but finding useful changes by hand requires repeated engineering and evaluation (Lin et al.,
2026; Xia et al., 2026). Recent work automates
this process through recursive self-improvement
(RSI), using execution feedback to repeatedly
propose, evaluate, and select harness edits (Lee
et al., 2026; Lin et al., 2026; Xia et al., 2026).
Although evolved harnesses can improve per-

Self-Improvement Memory Enables Continual Recursive Self-Improvement

formance on other benchmarks or models (Lin
et al., 2026; Wu et al., 2026; Xia et al., 2026; Xu
et al., 2026b), optimization is usually conducted
within a fixed setting. As models are updated
and agents encounter new tasks, harness optimization often needs to continue beyond that
setting. This raises two fundamental challenges.
Adapting to a new model. Model adaptation arises in two settings: multi-model serving,
where one shared harness supports different policy models, and model evolution, where new versions replace earlier ones within a model family.
Both motivate reusing an evolved harness and
its improvement experience instead of independently optimizing a harness for every model or
release. Yet modifications suited to one policy
can interact differently with another, even when
the benchmark stays fixed (Yang et al., 2026; Yu
et al., 2026d). In our workspace experiment, an
Opus-evolved harness starts at 68.41 on Gemini, below the seed harness’s 73.89 (Figure 4).
The optimizer must determine which inherited
mechanisms still help and which need revision.
Adapting to new data. With the policy fixed,
a different task distribution can expose failures
that source optimization did not address. A completion gate that checks whether commands ran
successfully, for example, may need to check
whether a feasible solution is also optimal. In
our text-classification experiment, the sourceevolved FewShotAll harness starts at 72.92 on
the target suite, below the seed’s 75.72 (Figure 3).
A useful source fix may therefore need revision
before it helps the target.
In either transition, the evolved harness alone
leaves important questions unanswered: why
was an edit proposed, what was it expected to
fix, and what happened when it was tested?
Source optimization produces this evidence, but
it need not accompany the harness. Without this
history, target optimization may repeat earlier
attempts or change inherited components without knowing their purpose. We therefore ask
whether the experience gained during source
optimization can help the harness adapt to new
models or data.
In this work, we study Continual Recursive

Self-Improvement (CRSI), in which harness
optimization continues after a benchmark or
policy-model change while preserving a compatible executable interface. We propose SelfImprovement Memory (SIM) to carry improvement experience alongside the evolved harness
(Figure 1). SIM groups selected edits by the harness problems they address and gives the proposer and selector access to their rationale, predicted and observed outcomes, and evaluation
context. It creates entries for new problems and
appends further attempts and outcomes to existing ones, helping the optimizer decide which
modifications to retain, revise, replace, or remove.
Our contributions are as follows:
• Continual harness optimization. We define
cross-dataset continuation with the policy
fixed and cross-model continuation with the
benchmark and split fixed. Existing harnessoptimization methods can use this setting
while retaining their proposal, evaluation,
and selection procedures.
• Self-Improvement Memory. We introduce a
structured record of harness problems, modifications, and outcomes that conditions both
proposal and selection, preserving source experience while incorporating new attempts
during target optimization.
• Controlled evidence across four domains.
With matched starting harnesses, round
counts, and candidate budgets, Full SIM outperforms harness-only and root-cause-only
continuation in six cross-dataset and four
Opus-to-Gemini settings. Across ten independent source runs in coding, paired continuations with SIM improve 9 of 10 runs, with a
mean advantage of 2.36 points over harnessonly continuation (p = 0.003).

2. Related Work
Recursive self-improvement of agent harnesses. Yu et al. (2026b) survey harness optimization workflows, recursive reuse, and
the conditions under which evolved modifications transfer. Meta-Harness and AHE search

2

Self-Improvement Memory Enables Continual Recursive Self-Improvement

over harness code using execution traces and
scores (Lee et al., 2026; Lin et al., 2026). Other
approaches let the agent modify its own system (Zhang et al., 2026a,b,d) or learn a policy for
editing harnesses (Shao et al., 2026). SIA instead
combines harness edits with updates to the task
model’s weights (Hebbar et al., 2026).
Transfer of evolved harnesses. Evolved harnesses can retain their gains on held-out tasks,
other models, or downstream benchmarks (Lee
et al., 2026; Lin et al., 2026; Shi et al., 2026).
Recent methods encourage transfer through
benchmark-disjoint evolution and modular edits (Wu et al., 2026), regularized search (Xia et al.,
2026), or separation of general and benchmarkspecific mechanisms (Yu et al., 2026a). Their
effectiveness still depends on how the model
and harness interact (Yang et al., 2026; Yu et al.,
2026d). PluginRSI also reuses its plugin library
in subsequent optimization.
Memory of the improvement process. Prior
work retains candidate artifacts (Lee et al.,
2026), edit histories (Xia et al., 2026), improvement graphs (Zhang et al., 2026c), skillrevision records (Li and Hu, 2026), and playbooks (Zhang et al., 2026f). HarnessBank groups
candidate harnesses by the problems they address (Luo et al., 2026). Xu (2026) continues
multi-task evolution with free-text notes and
source replay; Harness2 reuses an improvement
library across benchmarks (Xu et al., 2026a).
Meta-Skill and Meta2 transfer learned guidance
for constructing or editing task-specific harnesses (Qian et al., 2026; Yuan et al., 2026). Continual adaptation also raises retention and interference concerns (Chen et al., 2026; Zhao et al.,
2026). SIM links harness problems to modifications, predicted and observed outcomes, and
provenance. We test SIM by continuing optimization from the same evolved harness with
no SIM, root causes only, or the full record after a benchmark or model change. Appendix A
expands these comparisons, including continued optimization and memory for task-solving
agents.

3. Method
3.1. Problem Formulation
Harness RSI. Following Meta-Harness (Lee
et al., 2026), we optimize an executable harness
H around a fixed policy model M. The harness
determines the model’s context, tools, and execution flow. We write a setting as σ = ( M, X ),
with disjoint evolve and held-out evaluation sets
X evo and X eval . The score J ( H; M, X ) follows
the benchmark’s aggregation rule (Appendix B).
Only evolve-set feedback is available for proposing edits, selecting candidates, updating SIM, or
deciding when to stop.
A run consists of N rounds. At round t =
0, . . . , N − 1, the evaluator executes Ht on X evo
and returns scores, traces, and errors as Ft . The
proposer P uses Ft and the run’s history Dt (earlier feedback and code diffs) to generate k candidate harnesses Ct . The selector S screens proposals before execution and chooses among the
evaluated candidates, weighing performance,
complexity, domain specificity, and regression
risk:
Ct = P( Ht , Ft , Dt ),
(1)
Ht+1 = S( Ht , Ft , Ct , FtC ),
Here FtC contains feedback from the candidates
that passed screening and were executed. If no
candidate is accepted, Ht+1 = Ht . The proposer
and selector are LLM-based harness engineers;
M is the policy that executes the tasks.
Continual setting. After source RSI in σS =
( MS , XS ), optimization resumes from the final
retained harness HS in σT = ( MT , X T ). In crossdataset CRSI, the benchmark changes while the
policy stays fixed (XS ̸= X T , MS = MT ). In
cross-model CRSI, the policy changes on the same
benchmark and split (MS ̸= MT , XS = X T ).
Both require a shared executable harness interface. We measure target improvement as the
final minus starting score under J (· ; MT , X Teval ).
3.2. Self-Improvement Memory
SIM groups edits by the recurring harness problems they address. For a root-cause hypothesis
3

Self-Improvement Memory Enables Continual Recursive Self-Improvement

Evolve-set
tasks

Evaluator

Feedback
Ft

Candidate
harnesses

Proposer

Run M in Ht

Read code + history

Frozen policy

Propose k edits

Selector
Screen candidates

Ht(1) , … , Ht(k)

Verify + select

read SIM
history

record

History t

Self-Improvement Memory t

read SIM

Root cause, selected edit, rationale
Predicted / observed outcomes

Code, logs, diffs

Model, benchmark, round

Next round

Selected edit
+ outcome

Retained harness Ht + 1
Keep Ht if no edit is selected

Figure 2 | SIM in the agentic outer loop. Starting from ( HS , MS ), the proposer and selector consult
SIM (dashed arrows) to improve the harness on evolve-set tasks. After selection, SIM records the
chosen edit and its measured outcome (teal arrow). Held-out evaluation stays outside the loop.
ci , such as premature completion, an entry is

mi = ci , [( aij , oij , pij )] j ,
(2)
where j indexes attempts in order and Mt =
{mi } is the current memory. Each attempt stores
the modification and its rationale aij , predicted
and observed task outcomes oij , and provenance
pij (domain, benchmark, policy, and round).
Predictions of which tasks an edit will fix are
recorded before evaluation and checked afterward.
At each round, the proposer receives the complete SIM in its system prompt, and the selector reads the same record when assessing candidates. Both read all entries without retrieval or
truncation. The loop in Equation 1 becomes

Ct = P( Ht , Ft , Dt ; Mt ),
Ht+1 = S( Ht , Ft , Ct , FtC ; Mt ).

earlier attempts. If no edit is accepted, et = ∅
and U (Mt , ∅) = Mt . Entries with identical
root-cause text are merged without dropping
their histories. Appendix D.1 gives the entrymatching details.
3.3. Continual RSI via SIM
Source RSI starts with an empty SIM and produces ( HS , MS ). Full SIM carries both into target optimization (Figure 2). The proposer and
selector use each edit’s rationale, outcome, and
evaluation context to judge whether it still applies to the current failures. They can retain,
revise, replace, or remove harness modifications
while keeping the earlier memory records. Appendix D.2 gives the prompt instructions for using this history.

(3)

Each proposal cites an existing root cause or
names a new one. After selection, only the chosen candidate is recorded in et , including its measured outcomes even when the edit regresses
or fails to fix a predicted task. The update
Mt+1 = U (Mt , et ) appends this record to the
cited problem or creates a new entry, preserving

Transfer conditions. We compare four conditions: Cold Start ( H0 , ∅) from the seed harness;
Harness Transfer ( HS , ∅); Problem-Only Memory
( HS , McS ) with root causes only; and Full SIM
( HS , MS ). The three transfer conditions start
from the same HS , and all four use the same
target policy, tasks, and round and candidate
budgets. Each keeps its assigned memory condi4

Self-Improvement Memory Enables Continual Recursive Self-Improvement

tion throughout target RSI, while retaining the
ordinary target-run history Dt (Appendix C.3).
Source history enters through SIM; new target
records follow the same memory condition.

4. Experiments
Our experiments address four questions:

• Does SIM improve continued RSI after a
benchmark or policy-model change? (§4.2–
4.3)
• Does the full SIM record help beyond retaining only root causes? (§4.2 and §4.3.1)
• How does SIM guide the reuse and revision of
inherited harness edits? (§4.4; Appendix F.5)
• Is SIM’s benefit consistent across independently evolved source harnesses? (§4.4)
4.1. Experimental Setup
Domains. We study four domains in which a
source-evolved harness remains executable on
the target (Appendix B, Table 4). Coding moves
from Terminal-Bench 2.1 (TB2.1) to TerminalBench 4 (TB4) (Merrill et al., 2026; TerminalBench Team, 2026a,b), containerized shell tasks
scored by their own tests. Text classification
uses the online classification environment of
Meta-Harness (Lee et al., 2026), from a threedataset source suite to an eight-dataset target
suite absent from source RSI. Agentic workspace
moves from Harvey LAB (Harvey AI, 2026) to
the equal-weight mean of JobBench (Li et al.,
2026), GDPval (Patwardhan et al., 2026), and
APEX-Agents (Vidgen et al., 2026), using scoring
interfaces adapted from RRSI (Xia et al., 2026),
with Gemini 3.8 Flash as the judge. Engineering design moves from EngDesign (Guo et al.,
2025) to Frontier-Eng (Chi et al., 2026), scored
by frozen verifiers. Tasks are split uniformly at
random, without stratification, into evolve and
held-out sets of approximately equal size; exact
counts are in Appendix B. Only evolve-set scores
and trajectories reach the proposer, selector, and
SIM. The main comparisons use five rollouts per
task, with every rollout included in the score.

Transitions, models, and budgets. Crossdataset CRSI uses Gemini 3.8 Flash (Google
DeepMind, 2026b) as the policy in both stages.
For the cross-model transfer comparison, source
RSI uses Claude Opus 5.5 (Anthropic, 2026),
then Gemini 3.8 Flash continues on the same
benchmark and split. Both stages use the
target benchmarks listed above: TB4, the
eight-dataset classification suite, the merged
workspace benchmarks, and Frontier-Eng. Policy weights remain frozen. Gemini 3.8 Flash
also serves as proposer and selector in the main
comparisons. A source-RSI ablation replaces
it with Claude Opus 5.5 in these roles, yielding larger gains from both coding seeds (Appendix E.4.2, Table 7). The seeds are the minimal
AHE seed (Lin et al., 2026) and Terminus-2 (Merrill et al., 2026) for coding, NoMemory and FewShotAll (Lee et al., 2026) for text classification,
and a ReAct agent (Yao et al., 2023) over an MCP
tool gateway (Vidgen et al., 2026) for workspace
and engineering. For the latter two domains,
we adopt RRSI’s environments, seed harnesses,
and evaluation interfaces (Xia et al., 2026); Appendix C details our experimental setup. Every source and target run uses N = 10 rounds
with k = 5 candidate proposals per round in the
proposer–selector loop described in §3.1. Proposals rejected before execution receive no evaluation score; the five rollouts per task specify
the separate evaluation allocation.
Comparison conditions. Cold Start begins
from the seed harness without SIM. Harness
Transfer, Problem-Only Memory, and Full SIM
share the same source-evolved harness, with no
SIM, root causes only, and the complete record,
respectively. These memory conditions persist
throughout target optimization, with matched
target tasks, policy, round counts, and candidate
budgets (§3.3).
Metrics and reporting. Scores are on a 0–100
scale to two decimals: pass@1 for coding, accuracy pooled over examples for text classification,
benchmark-specific rubric, win-rate, and pass@1
scores for workspace, and pass rate or medal
score for engineering (Appendix B). Before and

5

Self-Improvement Memory Enables Continual Recursive Self-Improvement

after scores evaluate the starting harness and the
version retained after the final target round on
the held-out set. Except for the dedicated paired
study, each condition is one complete RSI run,
and its five rollouts per task estimate execution
performance rather than optimization variance.
We report individual settings descriptively and
use the ten-pair coding study to assess variation
across independent source runs (§4.4).
4.2. Cross-Dataset CRSI
SIM improves final scores in all six dataset
transitions. The memory ablation in Figure 3
compares continued optimization from the same
evolved harness with no SIM, root causes only,
or the full record. Full SIM finishes highest in all
six settings, exceeding Harness Transfer by 2.43–
4.35 points and Problem-Only Memory by 0.20–
6.06 points. Problem-Only Memory has mixed
effects: it ranges from 1.82 points below Harness
Transfer to 2.40 above it. Keeping the edit history and evaluation evidence thus helps beyond
retaining the diagnosis alone (Appendix E.4.1).
The margin over the strongest alternative
ranges from 0.20 points on NoMemory to 4.35 on
engineering. Section 4.4 tests whether the benefit recurs across independently evolved source
harnesses. Appendix E.2 lists the exact starting
and final scores for both transfer settings.
Source improvement does not ensure a better
target start. Source RSI raises held-out source
scores by 2.75–6.41 points in all six settings (Appendix E.1), yet the FewShotAll harness starts
target RSI below the seed: 72.92 versus 75.72.
Harness-only continuation reaches 74.12 and remains below Cold Start at 75.92, while Full SIM
reaches 77.92.
On NoMemory, Cold Start gains more than
Full SIM (3.40 versus 2.20 points) but finishes
lower (72.00 versus 73.60). We therefore report
both endpoints and use Harness Transfer, which
shares Full SIM’s initialization, as the direct control for the memory procedure.

Gemini model

Seed

Fresh RSI

CRSI

2.5 Flash
3.5 Flash
3.8 Flash
4 Argon

17.8
70.2
87.2
89.7

21.4
73.3
88.9
95.6

22.4
76.8
90.5
94.8

Table 1 | Success rates on held-out TB2.1 across
Gemini generations. Seed uses the unevolved
harness; Fresh RSI optimizes it independently.
CRSI adds SIM in the first generation and inherits the previous generation’s harness and SIM
thereafter. Bold compares Fresh RSI and CRSI.
4.3. Cross-Model CRSI
We examine transfer between model families,
continuation across model generations, and a
harness shared by multiple models.
4.3.1. Harness Transfer across Model Families
When the Opus-evolved harness is first run with
Gemini, it scores below Gemini’s seed harness
in every domain (Figure 4). The deficits range
from 0.60 points in text classification to 5.48 in
workspace. Target RSI does not always overcome this disadvantage: Harness Transfer still
finishes below Cold Start in three domains. Full
SIM finishes highest in all four and exceeds
harness-only continuation by 3.60–11.33 points.
It also finishes above Problem-Only Memory in
all four domains (Appendix E.4.1). Workspace
shows the largest difference: both begin at 68.41,
but Full SIM reaches 84.75 while Harness Transfer reaches 73.42.
4.3.2. Continual Improvement across Model
Generations
The generation chain carries the evolved harness
and SIM through successive Gemini models on
TB2.1 (Table 1; setup in Appendix C.5). Fresh RSI
starts from the seed at each generation. In the
first generation, both procedures use the same
seed, so that comparison tests SIM during the
initial run. Continuation improves over fresh RSI
in two of the three subsequent generations: by 3.5
points on Gemini 3.5 Flash and 1.6 on Gemini
3.8 Flash, while finishing 0.8 points lower on

6

Self-Improvement Memory Enables Continual Recursive Self-Improvement

Cold Start

Harness Transfer

Problem-Only Memory

Before target RSI
30
15

16.36

19.39

Held-out target score

20.61

24.85
18.18 18.79

18.18 19.39

18.18

19.39 19.39

0

(a) Coding / AHE
68.60 72.00

71.40 71.00

71.40 73.40

71.40 73.60

50

19.39 20.61

19.39

21.82

100

(b) Coding / Terminus-2
75.72 75.92

72.92 74.12

72.92 75.52

72.92 77.92

50

0

100

After target RSI
30
15

0

100

18.18

Full SIM (ours)

0

(c) Text cls. / NoMemory
73.89

82.98

74.93

85.07

74.93

85.54

74.93

87.89

(d) Text cls. / FewShotAll

60

39.13 42.61

39.13 40.87

50

39.13 42.61

39.13

46.96

30

0

0

(e) Workspace / ReAct

(f) Engineering / ReAct

Figure 3 | Cross-dataset CRSI: held-out target scores before (open bars) and after (filled bars) target
RSI. The three transfer conditions share the source-evolved harness; Cold Start uses the seed. Axis
limits vary by domain. Table 5 lists exact scores.
Cold Start

Harness Transfer

Problem-Only Memory

Before target RSI
30

Held-out target score

15

16.36

19.39
13.94

0

100

18.18

13.94

13.94

73.89

82.98

68.41 73.42

68.41

79.22

After target RSI
100

78.32 82.72

0

68.41

77.72 80.20

77.72 81.32

77.72 83.80

50

(a) Coding / AHE

50

0

21.82

20.61

Full SIM (ours)

84.75

(b) Text cls. / FewShotAll

60
39.13 40.87

34.78

42.61

50.43

46.96
34.78

34.78

30

(c) Workspace / ReAct

0

(d) Engineering / ReAct

Figure 4 | Cross-model CRSI from Opus 5.5 to Gemini 3.8 Flash, with benchmark and split fixed.
Open and filled bars show held-out scores before and after Gemini’s target RSI. Transfer conditions
share the Opus-evolved harness; Cold Start uses the seed (Table 6).

7

Self-Improvement Memory Enables Continual Recursive Self-Improvement

Harness construction

Evolve

Held-out

All

Run

Start

No SIM

SIM

∆

B1: Per-model harnesses
B2: Shared seed

77.40
72.36

75.20
73.28

76.30
72.82

S1: Sequential CRSI
S2: Unified synthesis

76.72
78.92

74.20
75.24

75.46
77.08

S3: Source policy used for RSI
Gemini 3.8 Flash
74.28
Grok 4.20 Reasoning
68.24
Claude Opus 5.5
75.20

71.24
66.84
72.24

72.76
67.54
73.72

1
2
3
4
5
6
7
8
9
10

18.18
16.97
17.58
18.18
17.58
19.39
18.79
18.18
19.39
19.39

20.61
17.58
20.00
18.18
18.79
20.00
20.00
20.00
18.18
20.00

22.42
19.39
20.61
23.64
20.61
23.64
21.82
19.39
23.03
22.42

+1.81
+1.81
+0.61
+5.46
+1.82
+3.64
+1.82
−0.61
+4.85
+2.42

Mean

18.36

19.33

21.70

+2.36

Table 2 | Text-classification scores averaged over
Grok 4.20 Reasoning, Claude Opus 5.5, and
Gemini 3.8 Flash. S3 rows name the policy used
to evolve each harness; each harness is evaluated
with all three models. All averages the equally
sized evolve and held-out splits. Bold marks the
highest mean in each column.

Table 3 | Paired coding continuations from ten
independent Terminus-2 source runs. Start is
the evolved harness’s held-out TB4 score; No
SIM and SIM are scores after ten target rounds.
∆ is SIM minus No SIM (mean +2.36; paired
p = 0.003).

Gemini 4 Argon.
4.3.3. One Harness for Multiple Models
We also ask whether one harness can serve Grok,
Opus, and Gemini on the text-classification target suite (Table 2; setup in Appendix C.6). We
compare sequential CRSI, unified synthesis using feedback from all three models, and transfer of harnesses evolved separately with each
policy. Unified synthesis reaches a similar mean
score to separately evolved harnesses: 75.24 versus
75.20 on held-out examples, above the shared
seed’s 73.28. Sequential CRSI reaches 74.20; the
three S3 harnesses average 66.84–72.24 across
the evaluation models. This descriptive comparison assesses a common harness; the matched
starting-harness comparisons in §4.3.1 test the
full SIM procedure.

times from Terminus-2 on TB2.1 and initialize
two ten-round TB4 runs from each resulting harness. Within each pair, the starting harness, policy, benchmark, and round and candidate budgets match. One run inherits that source run’s
SIM and appends target attempts; the other continues without SIM. The independent source run
is the unit of analysis.
SIM finishes higher in 9 of 10 pairs (Table 3),
with one pair favoring continuation without SIM
by 0.61 points. From a shared mean starting
score of 18.36, the mean final score is 21.70 with
SIM and 19.33 without it. The mean paired advantage is 2.36 points (95% CI [1.05, 3.68]; twosided paired t(9) = 4.06, p = 0.003). A twosided signed-rank check gives p = 0.006; the
paired standardized effect is dz = 1.28 (statistical details in Appendix C.4).

4.4. Analysis: The Role of SIM in CRSI
The paired comparisons test whether SIM improves continuation from a common starting
harness. We then follow individual memory
entries to see how earlier diagnoses inform later
edits.
SIM improves continuation from the same
evolved harness. We repeat source RSI ten

SIM guides reuse and revision of inherited edits. Full SIM and Harness Transfer inherit the
same completion gate from Terminus-2 source
RSI (Figure 11b, Appendix F.3). With SIM, the
proposer uses the gate’s rationale and source
outcomes to retain completion verification while
adding target checks, including feasibility versus optimality. Without SIM, the run tightens
the gate, twice repairs completion deadlocks,
8

Self-Improvement Memory Enables Continual Recursive Self-Improvement

Cold Start

Harness Transfer

Held-out TB4 score

26

Problem-Only Memory
26

24.85

24

24

22

22

20

20

18

18

16

21.82

16
0

2

4

6

8

Target RSI round

10

0

2

4

SIM − No SIM
(score points)

+4.85

+3.64
+1.81

+1.81

1

2

0

+1.82

+0.61

3

8

10

(b) Terminus-2 seed
+5.46

6

6

Target RSI round

(a) AHE seed

3

Full SIM

4

5

+2.42

+1.82

6

7

Independent source run

-0.61

8

9

Mean
+2.36

10

(c) Paired advantage across ten source runs

Figure 5 | Coding optimization (TB2.1→TB4). (a,b) Held-out TB4 scores of retained harnesses after
each target round; round 0 is the starting harness. (c) Final-score differences (SIM minus No SIM)
across ten paired continuations from independently evolved Terminus-2 harnesses. The dashed line
marks the mean; Table 3 gives individual scores.
and misattributes the inherited gate to its own
first round. The requirement carries over; its
implementation needs revision. Appendices F.5
and F.6 summarize transfer patterns across domains and models and the lessons for SIM.
SIM preserves diagnoses while adding target
evidence. P3 records a mismatch between deliverables and the verifier’s interface contract
(Figure 12; Appendix F.4). Target rounds 5 and 6
append revised checks and measured outcomes
under this diagnosis, keeping source attempts
and unresolved predictions available to later
rounds.
SIM supports earlier target progress and source
retention in coding. Full SIM is best or tied
throughout rounds 1–10 for both coding seeds
(Figure 5a,b). It exceeds the strongest control’s
final score (20.61) by round 5 from AHE and

round 2 from Terminus-2. In the AHE sourceretention trace, all transfer conditions start at
90.22 on held-out TB2.1 (Figure 8, Appendix E.3).
Full SIM loses 3 successful rollouts out of 225,
versus 4 for Problem-Only Memory and 6 for
Harness Transfer, while gaining more on TB4
than Problem-Only Memory (6.67 versus 0.61
points).

5. Conclusion
CRSI continues harness optimization when the
benchmark or policy model changes. SIM carries earlier diagnoses, edits, and outcomes into
this process and records new attempts. From
matched starting harnesses, Full SIM outperforms harness-only continuation in all six crossdataset settings and four Opus-to-Gemini domains. The ten-pair coding study finds a mean
advantage of 2.36 points across independent

9

Self-Improvement Memory Enables Continual Recursive Self-Improvement

source runs. The cases show how this history
helps the proposer and selector reuse earlier
reasoning while revising fixes for new requirements.

Limitations
Within our compute budget, independent RSI
repetitions focus on coding; the other domains
are evaluated with one run per condition. We
study settings with compatible harness interfaces and keep the optimizer’s planning and
search procedures fixed. Our comparisons evaluate SIM as a complete procedure, combining
inherited memory with updates during target
optimization.
Future work can extend the evaluation to
more repeated runs and longer transition sequences, and explore adaptation of planning,
token allocation, and tool interfaces.

Ethics Statement
LLM-based optimization agents rewrite harness
code in our experiments. The resulting harnesses run inside the benchmarks’ execution environments, with policy weights fixed and scores
computed by frozen verifiers or a fixed judging
procedure. A self-modifying harness could satisfy an evaluator without solving the intended
task. We keep held-out feedback away from
the optimization agents, identify each benchmark’s verifier or judge, and include an accepted edit that failed to repair its target tasks
(Appendix F.2). Workspace scores may also reflect biases of the LLM judge. The experiments
use existing publicly available benchmarks and
datasets.

References
L. A. Agrawal, S. Tan, D. Soylu, N. Ziems,
R. Khare, K. Opsahl-Ong, A. Singhvi,
H. Shandilya, M. J. Ryan, M. Jiang, C. Potts,
K. Sen, A. Dimakis, I. Stoica, D. Klein, M. Zaharia, and O. Khattab. GEPA: Reflective
Prompt Evolution Can Outperform Reinforcement Learning. In International Conference on

Learning Representations, 2026. URL https:
//proceedings.iclr.cc/paper_files/paper/
2026/hash/0e9e708b6f48e14fd0ac29e16741
3f76-Abstract-Conference.html.
Anthropic.
Introducing Claude Opus 5.5,
September 2026. URL https://www.anthropi
c.com/claude-opus-5-5.
J. Bai, L. Zhang, X. Yu, Y. Wu, Z. Wang, S. Li,
W. Li, Z. Zhao, L. Xue, K. Maeng, X. Fan,
and B. Peng. Verify Less, Evolve More:
Training Idea-Level Critics for VerificationEfficient ML Evolving Agents. arXiv preprint
arXiv:2610.08993, 2026. URL https://arxiv.
org/abs/2610.08993.
F. Barbieri, J. Camacho-Collados, L. E. Anke, and
L. Neves. TweetEval: Unified Benchmark and
Comparative Evaluation for Tweet Classification. In Findings of the Association for Computational Linguistics: EMNLP 2020, pages 1644–
1650, 2020. doi: 10.18653/v1/2020.findings-e
mnlp.148. URL https://aclanthology.org/2
020.findings-emnlp.148/.
I. Casanueva, T. Temčinas, D. Gerz, M. Henderson, and I. Vulić. Efficient Intent Detection
with Dual Sentence Encoders. In Proceedings
of the 2nd Workshop on Natural Language Processing for Conversational AI, pages 38–45, 2020.
doi: 10.18653/v1/2020.nlp4convai-1.5. URL
https://aclanthology.org/2020.nlp4conv
ai-1.5/.
X. Chen, Y. Huang, Y. Xu, Z. Zhao, E. McQuinn, J. Liu, and H. Yao. Are Self-Evolving
Agents Continual Learners? arXiv preprint
arXiv:2610.25858, 2026. URL https://arxiv.
org/abs/2610.25858.
Y. Chi, D. Hong, D. Jiang, T. Luo, et al.
Frontier-Eng: Benchmarking Self-Evolving
Agents on Real-World Engineering Tasks
with Generative Optimization. arXiv preprint
arXiv:2604.12290, 2026. URL https://arxiv.
org/abs/2604.12290.
A. Cohan, W. Ammar, M. van Zuylen, and
F. Cady. Structural Scaffolds for Citation Intent Classification in Scientific Publications. In
Proceedings of the 2019 Conference of the North
American Chapter of the Association for Computational Linguistics: Human Language Technologies,
10

