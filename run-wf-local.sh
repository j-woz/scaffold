#!/bin/bash

export PYTHONPATH=$PWD
export PYTHONUNBUFFERED=1
swift-t $* workflow.swift
