package algorythms;

import graph.interfaces.Graph;

import java.util.HashMap;
import java.util.Stack;

public class Kosaraju<U, V> {
    public Kosaraju(Graph<U, V> graph){
        Stack<U> stack = new Stack<>();
        HashMap<U, Boolean> visited = new HashMap<>();
        for(U vertex : graph.vertexSet()){
            visited.put(vertex, false);
        }
        for(U vertex : graph.vertexSet()){
            fillOrder(vertex, visited, stack, graph);
        }

        Graph<U, V> transposed = graph.getTransposed();

        for(U vertex : transposed.vertexSet()){
            visited.put(vertex, false);
        }

        while (!stack.empty()){
            
        }
    }
    private void fillOrder(U vertex, HashMap<U, Boolean> visited, Stack<U> stack, Graph<U, V> graph){
        visited.put(vertex, true);
        for(U neighbour : graph.getNeightbours(vertex)){
            if(!visited.get(neighbour)){
                fillOrder(neighbour, visited, stack, graph);
            }
        }
        stack.push(vertex);
    }
}
