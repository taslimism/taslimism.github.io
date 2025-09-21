+++
title = "Intro To Rerenders"
date = 2025-09-16
description = "let's say we have one heavy component and we want to add modal to that app."

[taxonomies]
# tags = ["react"]
categories = ["technical"]
+++

let's say we have one heavy component and we want to add modal to that app. so we set state in that component.
in react whenever a parent

<!-- more -->

component is rendered, all of its child component will also re-render, unless we wrap the child in useMemo.
