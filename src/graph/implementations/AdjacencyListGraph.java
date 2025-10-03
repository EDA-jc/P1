package graph.implementations;

import java.util.HashMap;
import java.util.Optional;
import java.util.Set;

import graph.abstracts.GraphBase;

public class AdjacencyListGraph<T, U>
        extends GraphBase<T, U> {
    //type restricted attributes


    private final HashMap<T, HashMap<T, Optional<U>>> vertex;
    //common methods
    public AdjacencyListGraph(boolean isDirected, boolean isWeighted){
        super(isDirected, isWeighted);
        vertex = new HashMap<>();
    }
    //type restricted methods
    @Override
    public void addVertex(T vertex) {
        this.vertex.put(vertex, new HashMap<>());
    }
    @Override
    public void removeVertex(T vertex) {
        this.vertex.remove(vertex);
    }
    public void addRelation(T first, T second){
        if(isWeighted())
            return;
        if(!hasVertex(first)||!hasVertex(second))
            return;

        this.vertex.get(first).put(second, Optional.empty());
        if(!isDirected())
            this.vertex.get(second).put(first, Optional.empty());
    }
    @Override
    public void addRelation(T first, T second, U weight) {
        if(!isWeighted())
            return;
        if(!hasVertex(first)||!hasVertex(second))
            return;

        this.vertex.get(first).put(second, Optional.of(weight));
        if(!isDirected())
            this.vertex.get(second).put(first, Optional.of(weight));

    }
    @Override
    public void removeRelation(T first, T second) {
        if(hasVertex(first)&&hasVertex(second))
            vertex.get(first).remove(second);
    }
    @Override
    public boolean hasRelation(T first, T second) {
        return this.vertex.get(first).containsKey(second);
    }
    @Override
    public int degreeOf(T vertex) {
        return this.vertex.get(vertex).size();
    }
    @Override
    public boolean hasVertex(T vertex) {
        return this.vertex.containsKey(vertex);
    }
    @Override
    public Set<T> getNeightbours(T vertex) {
        return this.vertex.get(vertex).keySet();
    }
    @Override
    public int size() {
        return this.vertex.size();
    }
    @Override
    public void showRelations() {
        vertex.forEach((src, edges) ->
                edges.forEach((dst, weight) ->
                        System.out.printf("%s --(%s)--> %s%n",
                                src,
                                weight.map(Object::toString).orElse(""),
                                dst)
                )
        );
    }
    @Override
    public void showVertex() {
        vertex.keySet().forEach(
                v-> System.out.println(v.toString())
        );
    }
}
