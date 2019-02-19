{% if params['numeric_strat'] in ['minmax', 'standard'] %}
{{ field }}_enc = encoders['{{ field }}_encoder'].transform(df['{{ field }}'].values)
{% endif %}

{% if params['numeric_strat'] in ['quantiles', 'percentiles'] %}
{{ field }}_enc = pd.cut(df['{{ field }}'].values, encoders['{{ field }}_bins'], labels=False, include_lowest=True)
{{ field }}_enc = encoders['{{ field }}_encoder'].transform({{ field }}_enc)
{% endif %}