---
layout: page
title: The Unix Shell
subtitle: Cluster Computing and PBS Commands
minutes: 25
---
> ## Learning Objectives {.objectives}
>
> * Understand how a cluster differs from a desktop computer
> * Be able to submit a job to a queue and check its status

A cluster computer is a supercomputer
constructed from individual cheap, replaceable computers,
called [nodes](reference.html#node),
that are linked by a fast network.
Each node has its own operating system,
usually a Linux variant.
In a typical setup,
one of the nodes in the cluster
is configured as the [head node](reference.html#head-node),
which acts as the controller for the cluster.
The remainder of the nodes
are configured as [compute nodes](reference.html#compute-node).
They perform work in the cluster.
Through the use of specially designed software,
the nodes of a cluster
act as a single computer.

A typical cluster is diagrammed here:

![A typical cluster computer configuration. (Public domain image from https://en.wikipedia.org/wiki/File:Beowulf.png)](fig/Beowulf.png)

Note how the outside world can only communicate with the cluster
through the server
(i.e., the head node, in the terminology we're using);
the compute nodes are hidden.
The head node is linked to the compute nodes
through a local network.
The head node and the compute nodes may also share
a locally networked storage device.

> ## Head node use {.callout}
>
> The head node is only to be used for
>
> * cluster access
> * job scheduling
> * communication with the compute nodes
>
> Heavy computational use may cause the head node to become unresponsive,
> limiting its availability to outside users
> and impeding job monitoring.
> Always use [PBS](reference.html#portable-batch-system) commands (below)
> to perform computational work on a cluster.

CSDMS maintains a cluster computer, ***beach***,
an SGI Altix XE1300 with 88 Altix XE320 compute nodes.
Each compute node is configured
with two quad-core 3.0 GHz E5472 (Harpertown) processors,
for a total of 704 cores.
Twenty-six of the 88 nodes have 4 GB of memory per core,
while the remainder have 2 GB of memory per core.
The cluster is controlled through an Altix XE250 head node.
Internode communication is accomplished through either gigabit ethernet
or over a non-blocking InfiniBand fabric.
Each compute node has 250 GB of local temporary storage.
All nodes are able to access 36 TB of RAID storage through NFS.

The typical way of working on a cluster
is to submit a [job](reference.html#job)
to the [scheduler](reference.html#scheduler)
that resides on the head node.
A job is organized as a script,
typically written in bash or in Python,
that contains commands to perform tasks.
If more than one job is scheduled,
they're assigned to a [queue](reference.html#job-queue) by the scheduler.
When adequate computing resources become available,
a job is popped off of the queue and run.
After the run completes,
any output can be collected
and transferred from the cluster
to a user's local computer.

The CSDMS cluster uses the
[TORQUE](http://www.adaptivecomputing.com/products/open-source/torque/)
job scheduler,
which employs [PBS](reference.html#Portable-Batch-System) commands
to submit and monitor jobs on the cluster.
Key PBS commands are:

* `qsub` to submit a job to the queue
* `qstat` to show the status of a job
* `qdel` to remove a job from the queue

Detailed information on these commands can be found
on their respective `man` pages; e.g.,

~~~ {.bash}
$ man qsub
~~~

To access the CSDMS cluster,
log into the head node of ***beach*** from your computer,
using the `ssh` ("secure shell") command:

~~~ {.bash}
$ ssh [username@]beach.colorado.edu
~~~

Be sure to replace `[username]` with the user name assigned to you
on ***beach***.
You'll be prompted for your password on ***beach***,
which is your CU IdentiKey.
A successful login will look something like this:

~~~ {.output}
Last login: Mon May  9 13:17:19 2016 from solaria.colorado.edu
]
] For assistance please mail trouble@colorado.edu
]

$
~~~
where the command prompt is now on ***beach***.
Check that you're in your home directory:

~~~ {.bash}
$ pwd
~~~

> ## Off-campus access to the CSDMS cluster {.callout}
>
> To access ***beach*** from outside of the CU-Boulder campus,
> you'll need to establish a Virtual Private Network (VPN) connection
> to the campus.
> The campus Office of Information Technology provides
> [instructions](http://www.colorado.edu/oit/services/network-internet-services/vpn)
> for downloading and installing VPN software.
> Once a VPN connection is established,
> you can connect to ***beach*** as above.

Next,
we need to transfer the files in the **code-shell** directory
from your local computer to ***beach***.
Open a new terminal window on your local computer,
change to your **Desktop** directory,
and get a directory listing:

~~~ {.bash}
$ cd ~/Desktop
$ ls
~~~

~~~ {.output}
code-shell  data-shell
~~~

To transfer the files,
we use the `scp` ("secure copy") command.
In the terminal on your local computer, type:

~~~ {.bash}
$ scp -r code-shell [username@]beach.colorado.edu:~
~~~

Here, the `-r` flag tells `scp` to recursively copy
the contents of the **code-shell** directory,
while the `~` at the end of the command
is the location to copy to on ***beach***,
your home directory.
Be sure to replace `[username]` with your ***beach*** user name.
You'll be prompted for your ***beach*** password.

In the terminal you've connected to ***beach***,
change to your home directory
and check that the files are present.

~~~ {.bash}
$ cd
$ ls
~~~

Next,
change to the **code-shell** directory
and list its contents:

~~~ {.bash}
$ cd ~/code-shell
$ ls
~~~

~~~ {.output}
calculate_pi.pbs.sh  calculate_pi.py  simple.pbs.sh
~~~

The file `simple.pbs.sh` is an example of a PBS script.
Dump the contents of this script to the terminal with `cat`:

~~~ {.bash}
$ cat simple.pbs.sh
~~~

~~~ {.output}
#!/usr/bin/env bash
# A simple PBS script. Submit this script to the queue manager with:
#
#  $ qsub simple.pbs.sh

echo "Hello world!"
~~~

This script,
when run,
will print "Hello world!"
to standard output.

Cluster computers often have several queues with different properties,
for example, a high-memory queue, a long run queue,
a debugging queue,
and a default queue.
View the queues available on the CSDMS cluster with `qstat`:

~~~ {.bash}
$ qstat -q
~~~

The `-q` flag prompts `qstat` to output only queue information.

~~~ {.output}
server: beach.colorado.edu

Queue            Memory CPU Time Walltime Node  Run Que Lm  State
---------------- ------ -------- -------- ----  --- --- --  -----
ocean-owner        --      --       --      --    0   0 --   E R
wrf-owner          --      --       --      --    0   0 --   E R
ocean-special      --      --       --      --    0   0 --   E R
route              --      --       --      --    0   0 --   E R
total              --      --       --      --    0   0 --   E R
wrf                --      --    12:00:00   --    0   0 --   E R
default            --      --    96:00:00   --  105  77 --   E R
himem              --      --       --      --    2  10 --   E R
debug              --      --    02:00:00   --    0   0 --   E R
long               --      --       --      --    0   0 12   E R
wrf-special        --      --       --      --    0   0 --   E R
vip                --      --    24:00:00   --    0   0 --   E R
ocean              --      --    12:00:00   --    0   0 --   E R
                                               ----- -----
                                                107  87
~~~

Submit this script to the scheduler with `qsub`:

~~~ {.bash}
$ qsub -q debug simple.pbs.sh
~~~

The scheduler returns a job id:

~~~ {.output}
197180.beach.colorado.edu
~~~

Ordinarily,
this job could be queried with `qstat`,
but this job runs really quickly.
In fact,
by the time you've read this,
it will have completed.



Interactive batch job.

Choosing a queue.

Email notification.

More information on submitting PBS jobs,
including examples,
can be [found](http://csdms.colorado.edu/wiki/HPCC_usage_rules)
on the CSDMS web site.


Check the all of the current jobs in all the queues on ***beach***
with the `qstat` command:

~~~ {.bash}
$ qstat
~~~

~~~ {.output}
Job ID                    Name             User            Time Use S Queue
------------------------- ---------------- --------------- -------- - -----
195567.beach               WBMsed3.11       frdu8933        295:39:1 R himem
195568.beach               WBMsed3.8        frdu8933        295:34:1 R himem
195569.beach               WBMsed3.5        frdu8933               0 Q himem
195570.beach               WBMsed3.2        frdu8933               0 Q himem
195571.beach               WBMsed3.10       frdu8933               0 Q himem
195578.beach               WBMsed3.3        frdu8933               0 Q himem
195972.beach               dem              jimc5170        24:54:08 R default
196667.beach               dem              jimc5170        45:57:19 R default
196670.beach               dem              jimc5170        44:18:05 R default
196673.beach               dem              jimc5170        44:31:45 R default
...
~~~



> ## Which compute nodes are being used? {.challenge}
>
> After you submit a PBS script to the scheduler,
> can you use `qstat` to find what compute node(s)
> your job is running on?
