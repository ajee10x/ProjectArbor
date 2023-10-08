#!/bin/bash

# Set the path to your LocalArborBuilder.sh script
LOCAL_ARBOR_SCRIPT="../LocalArborBuilder.sh"

# Define a function to run tests
run_test() {
    local input="$1"
    local expected_output="$2"
    local test_name="$3"

    local output
    output="$($LOCAL_ARBOR_SCRIPT $input)"

    if [ "$output" = "$expected_output" ]; then
        echo "Test $test_name: PASSED"
    else
        echo "Test $test_name: FAILED"
        echo "Expected Output: $expected_output"
        echo "Actual Output: $output"
    fi
}

# Test cases
test1_input="<Local Directory Path>"
test1_expected_output="local_project_tree.txt generated successfully."

test2_input="<Invalid Directory Path>"
test2_expected_output="Local directory not found."

# Run tests
run_test "$test1_input" "$test1_expected_output" "Valid Local Directory"
run_test "$test2_input" "$test2_expected_output" "Invalid Local Directory"
