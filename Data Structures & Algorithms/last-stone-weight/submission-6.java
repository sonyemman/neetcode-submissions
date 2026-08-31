class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());
        for (int stone: stones){ 
            priorityQueue.offer(stone);
        }
        
        while (priorityQueue.size() > 1) {
            Integer heaviest = priorityQueue.poll();
            Integer heaviest2 = priorityQueue.poll();

            if (heaviest != heaviest2) {
                int diff = heaviest - heaviest2;
                priorityQueue.offer(diff);
            }
        }

        priorityQueue.add(0);
        return priorityQueue.peek();
    }
}
