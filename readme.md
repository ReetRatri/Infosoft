
# Problem Description
The "Calendar" class was designed to allow users to schedule events without causing overlaps. However, the original implementation had issues in detecting overlaps and maintaining a binary tree structure.

# Issues Identified
1. Incorrect overlap-checking logic in `Node.insert`.
2. Incorrect traversal conditions for `left_child` and `right_child`.
3. Logical flaws leading to incorrect acceptance of overlapping events.

# Fixes Implemented
1. Updated the overlap condition to: `if node.start < self.end and node.end > self.start`.
2. Corrected tree traversal logic:
   - Left subtree for events ending before the current node starts.
   - Right subtree for events starting after the current node ends.
3. Ensured that the root initialization and subsequent insertions work seamlessly.

# Testing
The fixed code was tested with various cases to ensure correct behavior:
- Adding non-overlapping events works as expected.
- Overlapping events are rejected.
