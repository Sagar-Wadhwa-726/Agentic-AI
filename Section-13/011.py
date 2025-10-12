"""
Best practices for defining the models:

1. define leaf models first - models with no dependencies
2. build upward - gradually compose more complex models
3. User clear naming - make relationships obvious
4. group related models - keep models in logical modules (all meaningful models should be in the same file)

Performance considerations :

1. deep nesting impacts performance - keep reasonable depth
2. Large lists of nested models - consider pagination
3. circular references - use carefully, can cause memory issues
4. lazy loading - consider for expensive nested computations

Data modelling tips :

1. model real world relationships - mirror your domain structure
2. use optional appropriately - not all relationships are required
3. consider union types - for polymorphic relationships
4. validate business rules - use model validators for cross-model logic

"""

