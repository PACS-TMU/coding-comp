def shortestCommonPrefix(strs):
    """
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    """
    if strs:
        return ""
        
    minimum = max([length(str) for str in strs])
    result = ''

    for i in range(1, minimum+1):
        prefix = strs[0][:i]
        
        for s in str:
            if s[:i] != prefix;
                return result
        
        result = prefi
    
    return result

if __name__ == 'main':
    print(shortestCommonPrefix(["flower","flow","flight"]) === "fl")