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
            U vertex = stack.pop();
            if (!visited.get(vertex)) {
                // Cria lista para a componente atual
                HashMap<U, Boolean> componentVisited = new HashMap<>();
                for (U v : transposed.vertexSet()) {
                    componentVisited.put(v, false);
                }

                // Colete os vértices da SCC
                Stack<U> sccStack = new Stack<>();
                dfsCollect(vertex, visited, sccStack, transposed);

                // Imprime ou armazena a SCC
                System.out.println("Componente fortemente conexa: " + sccStack);
            }
        }
    }

    private void dfsCollect(U vertex, HashMap<U, Boolean> visited, Stack<U> sccStack, Graph<U, V> graph) {
        visited.put(vertex, true);
        sccStack.push(vertex);
        for (U neighbour : graph.getNeightbours(vertex)) {
            if (!visited.get(neighbour)) {
                dfsCollect(neighbour, visited, sccStack, graph);
            }
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
