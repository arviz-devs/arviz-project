(roadmap)=
# Roadmap

Last updated: April 2023

## Our philosophy
As stated in our homepage:

> ArviZ is an open source project aiming to provide tools for Exploratory Analysis of Bayesian Models that do not depend on the inference library used.

In this page we describe our current roadmap and high-level actions to work towards this goal.

## Project roadmap
We believe both ArviZ and Exploratory Analysis of Bayesian Models are currently relatively established concepts.
Therefore, generally speaking, as a project we are working on changing ArviZ paradigm/design
from monolithic functions that generate complete analyses and visualizations towards
being more modular.

At the same time, we plan to equally prioritize all three tasks of: library development,
publishing documentation, and growing and encouraging participation.

### Library development

This includes both maintenance and bug fixing of our existing libraries and extending the
capabilities of these libraries (or creating new ones) in order to improve the toolset for
Exploratory Analysis of Bayesian Models that is available to practitioners.

This point is library dependent so it is detailed below for each of the different libraries
of the ArviZ project.

### Publishing documentation
By "documentation" here we understand both documentation on how to use the libraries themselves
and educational material on how to perform Exploratory Analysis of Bayesian Models on a conceptual level.

### Growing and encouraging participation
The focus of this point is ensuring all {ref}`ArviZ team members <our_team>` are engaged
according to their own possibilities, i.e. we are not setting barriers on participation
nor growth due to ArviZ culture or leadership.

Also making sure everyone feels their contributions are values,
whether they are code contributions, helping with social media,
coordinating sprints/workshops/forum participation...
In 2023 we will have our 2nd Random Variables council election.
We would like to encourage participation, aiming to continue acting thoughtfully given
the interests of different inference libraries that ArviZ works with.

Lastly, and to a lesser extent given it is somewhat conditioned on the other points,
also continue onboarding new people, especially with different backgrounds, interests and expertise join the team.
To this end, we are planning to participate in internship projects,
continue to hire for specific small projects that require expertise not currently present in our team,
and take part in or organize sprints, office hours or working sessions to attract and support people in joining the team.

---

## Python roadmap
For Python, the move towards modular design is happening at the same time within the main ArviZ Python library and
with the creation of new libraries.

### ArviZ main Python library
We plan to refactor the plotting and stats modules so they become more independent and modular themselves.
This will ease adding new visualizations and statistics/diagnostics and at the same time should also
serve as breadcrumbs for the other new libraries like ArviZ dashboards or PreliZ.

Our goal is to separate the data organization, data processing and plotting steps.

* Data organization: given faceting and aesthetics mapping instructions, divide the input data and map aesthetics accordingly.
* Data processing: compute statistics and diagnostics via xarray _using any of its compatible array computation libraries_.
* Plotting: Interact with plotting backends through a common interface layer. Thus, plotting functions will be unique,
  without need for repeating/adapting them to each backend, and each backend would only need to implement the common interface layer.

We belive that this design will allow ArviZ to continue to provide end-to-end visualizations and make it easier to add new ones to the
library, while at the same time providing reusable lower level visual and computation functions for users to generate
their own custom end-to-end visualizations or for developers to build new libraries on (e.g. ArviZ dashboards).

### PreliZ
We recently submitted a paper on PreliZ to JOSS which, at the time of writing, is waiting for reviews.
During 2023 we plan to start advertizing the library even if not yet full-featured to
get users and see how it fares in real world prior elicitation tasks.

In addition to maintenance and improvement of current capabilities of PreliZ,
we will also experiment on multivariate elicitation strategies.

### ArviZ dashboards
We plan to dedicate significant resources to the development of dashboards and dashboard components
in the coming years. To make this possible we will ask for some grants to ensure we have dedicated
time to finish the refactoring and work on ArviZ dashboards. Refactoring is related to this point
because it will make dashboard development possible and faster (where it already is possible).

We also plan to expand our expertise so we become more efficient at designing, implementing and
documenting dashboards.

---

## Julia roadmap
As Python functionality is ported to Julia, it is divided into smaller, modular packages that are designed to
- be standalone packages useful outside of ArviZ,
- integrate with the broader Julia ecosystem, and
- interact well with ArviZ.jl's data structures.
Examples of these packages are PSIS.jl, InferenceObjects.jl, and MCMCDiagnosticTools.jl. ArviZ.jl is then primarily a monopackage that brings all of these components together.

The main development priority in Julia in 2023 is porting plots with both the Plots.jl and Makie.jl backends and providing utilities to support bespoke plotting.

Our goal is to build and maintain ArviZ as an ecosystem of small topic/domain specific libraries.
