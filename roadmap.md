(roadmap)=
# Roadmap

Last updated: February 2023

## Our philosophy
As stated in our homepage:

> ArviZ is an open source project aiming to provide tools for Exploratory Analysis of Bayesian Models that do not depend on the inference library used.

In this page we describe our current roadmap and specific actions to work towards this goal.

## Project roadmap
We believe both ArviZ and Exploratory Analysis of Bayesian Models are currently relatively established concepts.
Therefore, generally speaking, as a project we are working on changing ArviZ paradigm/design
from monolithic functions that generate complete analyses and visualizations towards
being more modular.

At the same time, we plan to equally prioritize all three tasks of:
- Library development
- Publishing documentation
- Growing and encouraging participation in the library
In 2023 we will have our 2nd Random Variables council election. We would like to encourage participation,
aiming to continue acting thoughtfully given the interests of different inference libraries that ArviZ works with.

And we would like to continue having more people with different backgrounds, interests and expertise join the team.
To this end, we are planning to participate in internship projects, continue to hire for specific small projects
that require expertise not currently present in our team, and take part in or organize sprints, office hours or working sessions
to attract and support people in joining the team.

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
Publish paper, start advertizing the library to get users and get real world tests, add some multivariate elicitation strategies?

### ArviZ dashboards
Plan to ask dashboard + some refactoring grant

## Julia roadmap
As Python functionality is ported to Julia, it is divided into smaller, modular packages that are designed to
- be standalone packages useful outside of ArviZ,
- integrate with the broader Julia ecosystem, and
- interact well with ArviZ.jl's data structures.
Examples of these packages are PSIS.jl, InferenceObjects.jl, and MCMCDiagnosticTools.jl. ArviZ.jl is then primarily a monopackage that brings all of these components together.

The main development priority in Julia in 2023 is porting plots with both the Plots.jl and Makie.jl backends and providing utilities to support bespoke plotting.

Our goal is to build and maintain ArviZ as an ecosystem of small topic/domain specific libraries.
