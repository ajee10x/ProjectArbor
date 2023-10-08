#!/bin/bash

# Set the path to your ArborBuilder.sh script
ARBOR_SCRIPT="../ArborBuilder.sh"

# Define a function to run tests
run_test() {
    local input="$1"
    local expected_output="$2"
    local test_name="$3"

    local output
    output="$($ARBOR_SCRIPT $input)"

    if [ "$output" = "$expected_output" ]; then
        echo "Test $test_name: PASSED"
    else
        echo "Test $test_name: FAILED"
        echo "Expected Output: $expected_output"
        echo "Actual Output: $output"
    fi
}

# Test cases
test1_input="<GitHub Username> <GitHub Repository Name>"
test1_expected_output="github_project_tree.txt generated successfully."

test2_input="<Invalid Username> <Invalid Repository>"
test2_expected_output="GitHub repository not found."

# Run tests
run_test "$test1_input" "$test1_expected_output" "Valid GitHub Repository"
run_test "$test2_input" "$test2_expected_output" "Invalid GitHub Repository"
