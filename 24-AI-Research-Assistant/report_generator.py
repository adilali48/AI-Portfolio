from agent import llm


def generate_report(topic, context):

    prompt = f"""
You are a professional research assistant.

Write a detailed research report.

Topic:
{topic}

Research Information:
{context}

Use the following format:

# Title

## Introduction

## Overview

## Key Findings

## Advantages

## Challenges

## Future Scope

## Conclusion

Write professionally.
"""

    response = llm.invoke(prompt)

    return response.content