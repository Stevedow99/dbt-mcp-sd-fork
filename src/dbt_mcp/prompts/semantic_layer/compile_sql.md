Get compiled SQL for metrics from the dbt Semantic Layer without executing the query.

This tool allows you to retrieve the SQL that would be executed when querying the dbt Semantic Layer, without actually running the query. This is useful for understanding how metrics are transformed into SQL, debugging issues, or inspecting the generated SQL before execution.

You can specify metrics to include and group by dimensions with optional grain.

Example:
```
compile_sql(
  metrics=["food_order_amount", "order_gross_profit"],
  group_by=[{"name": "metric_time", "grain": "MONTH"}, {"name": "customer__customer_type"}]
)
```

This will return the SQL that would be used to query these metrics and dimensions, but won't execute the query.
