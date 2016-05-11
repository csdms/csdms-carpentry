#!/usr/bin/env bash
# A PBS script that calls a Python script that calculates an
# approximation to pi. Submit this script to the queue manager with:
#
#  $ qsub calculate_pi.pbs.sh

cd $PBS_O_WORKDIR
echo "Calculating pi with the Bailey–Borwein–Plouffe formula"
echo "Start time:" `date`
python calculate_pi.py 20
echo "End time:" `date`
