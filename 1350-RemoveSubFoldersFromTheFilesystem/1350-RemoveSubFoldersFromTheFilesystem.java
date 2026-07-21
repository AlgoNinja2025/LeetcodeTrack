// Last updated: 7/21/2026, 7:09:00 PM
class Solution {
    public List<String> removeSubfolders(String[] folder) {
         Set<String> dirSet = new HashSet<>();
        List<String> res = new ArrayList<>();

        for (String dir : folder)
            dirSet.add(dir);

        for (String dir : folder) {
            res.add(dir);
            for (int i = 0; i < dir.length(); i++) {
                if (dir.charAt(i) == '/' && dirSet.contains(dir.substring(0, i))) {
                    res.remove(res.size() - 1);
                    break;
                }
            }
        }

        return res;
        
    }
}