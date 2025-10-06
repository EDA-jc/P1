package graph.abstracts;

import graph.interfaces.Graph;

public abstract class GraphBase<T, U>
        implements Graph<T, U> {
    //common attributes
    private final boolean isDirected;
    private final boolean isWeighted;

    protected GraphBase(boolean isDirected, boolean isWeighted) {
        this.isDirected = isDirected;
        this.isWeighted = isWeighted;
    }
    @Override
    public boolean isDirected() {
        return isDirected;
    }
    public boolean isWeighted(){
        return isWeighted;
    }

}
