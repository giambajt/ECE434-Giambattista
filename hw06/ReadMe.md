HW06 questions

1.	Where does Julia Cartwright work?
National Instruments
2.	What is PREEMT_RT? Hint: Google it.
A new preempting system for linux to remove unbounded latencies to increase speed
3.	What is mixed criticality?
A system that runs both time critical and non time critical tasks
4.	How can drivers misbehave?
Drivers can misbehave by taking too much CPU time away from time critical events
5.	What is Δ in Figure 1?
The time it takes for a task to run after some event has occurred
6.	What is Cyclictest[2]?
A test that measures the latency between and event and a task by measuring the time, running a task and then measuring the time again when the thread finishes
7.	What is plotted in Figure 2?
Figure 2 plots the Δ spikes for time and we can see there are more long latency spikes for normal preempt but there the latency is always under 16us for preempt_rt
8.	What is dispatch latency? Scheduling latency?
The dispatch latency is the time between the event happening and the scheduler being told to run a thread.  Scheduling latency is the time it takes for the scheduler to actually load the thread onto the CPU
9.	What is mainline?
	The main, stable kernel releases that everyone can use
10.	What is keeping the External event in Figure 3 from starting?
The non critical IRQ is keeping the external event from running.  In this figure, the less important IRQ must finish before the external event can be scheduled.
11. Why can the External event in Figure 4 start sooner?
	The little purple bar is a very small portion of code that will wake up the necessary thread so in the case of a higher priority event, now that less critical thread can be preempted and the more critical thread can be scheduled.




