import pandas as pd

state_list = ['California', 'Texas', 'Florida', 'New York', 'Illinois',
              'Pennsylvania', 'Ohio', 'Georgia', 'North Carolina', 'Michigan',
              'New Jersey', 'Virginia', 'Washington', 'Arizona', 'Massachusetts',
              'Tennessee', 'Indiana', 'Missouri', 'Maryland', 'Wisconsin',
              'Colorado', 'Minnesota', 'South Carolina', 'Alabama', 'Louisiana',
              'Kentucky', 'Oregon', 'Oklahoma', 'Connecticut', 'Utah', 'Iowa',
              'Nevada', 'Arkansas', 'Mississippi', 'Kansas', 'New Mexico',
              'Nebraska', 'West Virginia', 'Idaho', 'Hawaii', 'New Hampshire',
              'Maine', 'Montana', 'Rhode Island', 'Delaware', 'South Dakota',
              'North Dakota', 'Alaska', 'DC', 'Vermont', 'Wyoming']

population_list = [39512223, 28995881, 21477737, 19453561, 12671821, 12801989,
                   11689100, 10617423, 10488084, 9986857, 8882190, 8535519,
                   7614893, 7278717, 6949503, 6833174, 6732219, 6137428,
                   6045680, 5822434, 5758736, 5639632, 5148714, 4903185,
                   4648794, 4467673, 4217737, 3956971, 3565287, 3205958,
                   3155070, 3080156, 3017825, 2976149, 2913314, 2096829,
                   1934408, 1792147, 1787065, 1415872, 1359711, 1344212,
                   1068778, 1059361, 973764, 884659, 762062, 731545, 705749,
                   623989, 578759,]

state_series = pd.Series(data=population_list,
                         index=state_list,
                         dtype='int64')

type(state_series)
