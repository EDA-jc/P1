import algorythms.DFS;
import entity.Client;
import graph.implementations.AdjacencyListGraph;
import graph.interfaces.Graph;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        Graph<String, Double> graph = new AdjacencyListGraph<>(true, true);
        Client julio = new Client("julio");
        Client anderson = new Client("anderson");
        graph.addVertex("julio");
        graph.addVertex("anderson");
        graph.addRelation("julio", "anderson", 2.0);
        new DFS<>(graph);
    }
}