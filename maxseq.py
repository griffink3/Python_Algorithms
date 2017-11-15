#!/usr/bin/python
class InvalidInputException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def maxseq(array):
    """array_less_than: any[] -> int
    Consumes: one python list
    Produces: the greatest sum of a subarray + 180
    Example: maxseq([-1, 2, 7, -8, 13, -2]) -> 194
             maxseq([-7, -9, -10]) -> 180
             maxseq([10, -5, 200]) -> 385
    """

    # error checking on input array -- is it valid?
    if array is None:
        raise InvalidInputException("array is None (invalid)")

    overallMax = 0 # Variable to keep track of the overall max gain
    prevMax= 0 # Variable to keep track of the previous sequence of consecutive gains
    currMax = 0 # Variable to keep track of the current sequence of consecutive gains
    currNegs = 0 # Variable to keep track of the current sequence of consecutive losses

    """For every positive element we add it to the current max but if the
    next element is negative, this signals the end of the sequence, so
    first we check if it's greater than the overall max. Then we check if
    this current max added to the sequence of losses before and the sequence
    of gains before those losses is greater than the overall max. In either
    case, if true, we set the overall max equal to the value we compare to it.
    In either case, whether true or false, we then set the previous max to
    the current max and the current max to 0, later to be filled by the next
    sequence of consecutive gains.

    For every negative element, we add it to the current negatives
    to keep track of consecutive losses. However, before that, if the previous
    element was positive, we set the current negatives to 0 in order to start
    afresh.

    At the end, we return the overall max or the greatest gain added to 180.
    """
    for i in range(len(array)):
        if array[i] > 0:
            currMax = currMax + array[i]
            if i == len(array)-1: # Don't want to check for the next one if we're at the end
                # But we still want to compare values
                if currMax > overallMax:
                    overallMax = currMax
                if currMax + currNegs + prevMax > overallMax:
                    overallMax = currMax + currNegs + prevMax
            elif array[i+1] < 0: # Only checks if next element is negative if not at the end
                if currMax > overallMax:
                    overallMax = currMax
                if currMax + currNegs + prevMax > overallMax:
                    overallMax = currMax + currNegs + prevMax
                prevMax = currMax
                currMax = 0
        if array[i] < 0:
            if i > 0 and array[i-1] > 0:
                currNegs = 0
            currNegs = currNegs + array[i]

    return overallMax + 180
