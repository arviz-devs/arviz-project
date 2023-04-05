(processes)=
# Election and decision making processes

(contributor_onboarding)=
## New Contributor Nominations and Confirmation Process
Current Contributors can nominate candidates to become Contributors by
requesting so in a GitHub issue at [arviz-project repository](https://github.com/arviz-devs/arviz-project/issues?q=is%3Aissue+label%3Agovernance),
constraints on eligibility are detailed in the role descriptions.
The log of past nominations and their results is kept available in that repository.

If nominated, candidates accept their nomination
(explicit comment approving nomination on the issue or "thumbs-up" emoji on the same issue),
then they can be considered by the Council: on the first of the month following a
nomination, the Council will vote on each nominee using {ref}`this process <council_voting>`.

:::{note}
In the case of recurring contributors, the nomination and voting process can be replaced
by a somewhat similar selection process. Thus, for example, GSoC interns are considered
recurrent contributors once accepted; similarly, contractors hired thanks
to grants like CZI EOSS or GSoD ones are also considered recurrent contributors once
hired.
:::

Voting will be private with results published on the issue ticket. In the case of a
rejection, results must include the reasons behind the decision (e.g. the time since
starting to contribute is deemed too short for now). The candidate
would then have to wait 3 months to be considered again.

(council_decision_process)=
## Council Decision Making Process
By and large we expect the decisions in ArviZ to be made _ad hoc_ and require little formal
coordination and with the community at large. However, for controversial proposals and
new Core Contributors the council may need to intervene to make the final decision
in a group vote.

(call_for_vote)=
### Call for a vote
Core Contributors can call for a vote to resolve a target issue they feel has
been stale for too long and for which informal consensus appears unlikely. For a vote
to be called, the target issue must be at least 2 months old.

To do so, they have to open a proposal issue ticket labeled "Council Vote".
The proposal issue should contain a link to the target issue and a proposal
on how to resolve it. Proposals should include a statement making clear what it
means to "agree" or to "disagree".

Before voting starts, at least 3 days will be left for Core
Contributors to raise doubts about the proposal's _phrasing_, no extra discussion will take
place in the proposal issue. Proposal issues should be locked from creation
to prevent attracting discussion from people not familiar with the decision
process.

(council_voting)=
### Voting process

* Each Council Member will vote either "Yes", "No", or "Neutral".
* It is recommended that all Council Members expose their reasons when voting.
  "No" votes, however, _must_ list the reasons for disagreement. Any "No" vote
  with no reason listed will be considered a "Neutral" vote.
* An absence of vote is considered as "Neutral".
* Voting will remain open for at least 3 days.
* For the proposal to pass, at least 60% of the council must vote "Yes", and no more
  than 20% can vote "No".

For decisions about the project the Council will perform it directly on the
proposal issue.
For decisions about people, such as electing or ejecting Core Contributors, the Council
will vote privately. However the decision will be posted publicly in an issue ticket.

## Private communications of the Council

Unless specifically required, all Council discussions and activities will be
between public (GitHub, Gitter), and partially public channels (Slack)
and done in collaboration and discussion with the rest of the ArviZ team
and the Community. The Council will have a private channel that will be used
sparingly and only when a specific matter requires privacy. When private
communications and decisions are needed, the Council will do its best to
summarize those to the Community after eliding personal/private/sensitive
information that should not be posted to the public internet.

## Conflict of interest

It is expected that Council Members will be employed at a wide
range of companies, universities and non-profit organizations. Because of this,
it is possible that Members will have conflict of interests. Such conflict of
interests include, but are not limited to:

-   Financial interests, such as investments, employment or contracting work,
    outside of The Project that may influence their work on The Project.
-   Access to proprietary information of their employer that could potentially
    leak into their work with the Project.

All members of the Council shall disclose to the rest of the
Council any conflict of interest they may have. Members with a conflict of
interest in a particular issue may participate in Council discussions on that
issue, but must recuse themselves from voting on the issue.

(council_selection)=
## Council Selection Process

### Eligibility
* Must be core contributor for at least one year

### Nominations
* Nominations are taken over a public GitHub issue ticket over the course of 2 weeks.
* Only Core Contributors may nominate folks
* Self Nominations are allowed
* At the conclusion of the 2 weeks, the list of nominations is posted on the ticket and this ticket is closed.


### Election Process

(initial_voting_election)=
* Voting occurs over a period of at least 1 week, at the conclusion of the nominations.
  Voting is blind and mediated by either an application or a third party like NumFOCUS.
  Each voter can vote zero or more times, once per each candidate. As this is not about
  ranking but about capabilities, voters vote on a yes/neutral/no basis
  per candidate -- “would I trust this person to lead ArviZ?”.
  - All core contributors can vote in an election.
* Candidates are evaluated independently, each candidate having 60% or more of
  yes votes _and_ less or equal than 20% of no votes is chosen.
  If the council resulting from all accepted candidates matches all conditions
  described in {ref}`this section <council_description>` all candidates are
  confirmed and the election process stops here.
* In the event that either not enough or too many candidates were confirmed,
  candidates are ranked by interpreting yes=+1, neutral=0 and no=-1. If too
  many candidates were confirmed, the 7 candidates with higher rank are
  elected. If not enough candidates were chosen, the 4 candidates with higher
  rank are elected. If affiliation conditions were not met, multiple potential
  councils will be constructed with candidates whose rank is `>i` for all possible
  values of `i`. If any of those potential councils matches the conditions,
  the one with smaller `i` will be chosen.

  :::{admonition} Example
  :class: dropdown

  If there were 9 accepted candidates out of a team of 12 people.
  Their affiliations are `A, B, B, C, A, A, B, D, E`.
  There more than 7 accepted candidates, so the first step would be to attempt
  selecting the 7 with higher rank. They all had 8 or more "Yes" votes,
  and 2 or less "No" votes, so their ranks will go between 12 and 6.
  Their ranks are respectively `12, 12, 12, 10, 10, 9, 8, 7, 6`.

  The council integrated by the 7 candidates with higher rank would have
  3 people reporting to both company A and B, so it doesn't match all
  conditions either. We therefore evaluate 3 alternative potential councils:

  * rank 9 or higher: 6 members, still 3 people report to the same company,
    now only to company A but doesn't match the conditions either.
  * rank 10 or higher: All conditions are met.
  * rank 12 or higher: Only 3 candidates left, but the council must be 4 people at least.

  We would then end up with a 5 people council, with members with rank 10 or higher.

  Alternatively, if the ranks had been `12, 12, 12, 10, 9, 9, 8, 7, 6`,
  we would still choose the council of candidates with rank 10 or higher,
  as otherwise not all conditions are met, but in that case it would be a
  4 people council

  If the ranks had been `12, 12, 12, 10, 10, 10, 8, 7, 6`, then the process would
  continue, with the {ref}`run off election <run_off_election>` between
  the 3 tied candidates with rank 10.
  :::

  (run_off_election)=
* In the event of a tie there will be a runoff election for the tied candidates. To avoid
  further ties and discriminate more among the tied candidates, this vote will be held
  by [Majority Judgment](https://en.wikipedia.org/wiki/Majority_judgment) (MJ): for each
  candidate, voters judge their suitability for office as either "Excellent", "Very Good",
  "Good", "Acceptable", "Poor", or "Reject". Multiple candidates may be given the same
  grade by a voter. The candidate with the highest median grade is the winner.
* If more than one candidate has the same highest median-grade, the MJ winner is
  discovered by removing (one-by-one) any grades equal in value to the shared median
  grade from each tied candidate's total. This is repeated until only one of the
  previously tied candidates is currently found to have the highest median-grade.
* If ties are still present after this second round, the winner will be chosen at random.
  Each person tied will pick an integer number in the `[1, 100]` interval and send it
  privately to the third party mediating the election. After receiving all the numbers,
  said third party will draw a random integer from random.org. The person with the
  closest circular distance, defined as `min(|a-b|, 100-|a-b|)`, will be selected.
  This process will be repeated as many times as necessary as there may be ties
  resulting from candidates choosing the same number.
* At the conclusion of voting, all the results will be posted. And at least 24
  hours will be left to challenge the election result in case there were
  suspicions of irregularities or the process had not been correctly carried
  out.

## Vote of No Confidence
* In exceptional circumstances, council members as well as core contributors may remove a sitting council member via a vote of no confidence. Core contributors can also call for a vote to remove the entire council -- in which case, Council Members do not vote.
* A no-confidence vote is triggered when a core team member (i.e Council member or Core contributor) calls for one publicly on an appropriate project communication channel, and two other core team members second the proposal. The initial call for a no-confidence vote must specify which type is intended -- whether it is targeting a single member or the council as a whole.
* The vote lasts for two weeks, and the people taking part in it vary:
  * If this is a single-member vote called by Core contributors, both Council members and Core contributors vote, and the vote is deemed successful if at least two thirds of voters express a lack of confidence.
  * If this is a whole-council vote, then it was necessarily called by Core contributors (since Council members can’t remove the whole Council) and only Core contributors vote. The vote is deemed successful if at least two thirds of voters express a lack of confidence.
  * If this is a single-member vote called by Council Members, only Council Members vote, and the vote is deemed successful if at least half the voters express a lack of confidence. Council Members also have the possibility to call for the whole core team to vote (i.e Council members and Core contributors), although this is not the default option. The threshold for successful vote is also at 50% of voters for this option.
* If a single-member vote succeeds, then that member is removed from the council and the resulting vacancy can be handled in the usual way.
* If a whole-council vote succeeds, the council is dissolved and a new council election is triggered immediately.

## Ejecting Core Contributors
* Core contributors can be ejected through a simple majority vote by the council. Council members vote "Yes" or "No".
* Upon ejecting a core contributor the council must publish an issue ticket, or public document detailing the
  * Violations
  * Evidence if available
  * Remediation plan (if necessary)
  * Signatures majority of council members to validate correctness and accuracy

## Leaving the project
Core contributors can also voluntarily leave the project by notifying the community through a public means or by notifying the entire council.

Unless they request otherwise, they will be listed on {ref}`emeritus` page.
