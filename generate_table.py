import pandas as pd

data = pd.read_csv('data.csv') # import data to pandas from data.csv

# Get coefficients for the curve fits
loggerA = data['Logger A'].tolist()
loggerC = data['Logger C'].tolist()
loggerB = data['Logger B'].tolist()

# curve fit: V(t)=A*e^(-Ct)+B
logger_equations = []
for i in range(len(loggerA)):
    # round to 3 decimal places for printing
    formatted_logger_a = str(round(loggerA[i], 3))
    formatted_logger_c = str(round(loggerC[i], 3))
    formatted_logger_b = str(round(loggerB[i], 3))
    # Replace A, C, and B with the rounded values
    latex_formatted_equation = str(r'$V(t)=Ae^{-Ct}+B$').replace('A', formatted_logger_a).replace('C', formatted_logger_c).replace('B', formatted_logger_c)
    logger_equations.append(latex_formatted_equation) # add to list

# Get coefficients for the theoretical curves
theoreticalA = data['Theoretical A'].tolist()
theoreticalC = data['Theoretical C'].tolist()

# curve: V(t)=A*e^(-Ct)
theoretical_equations = []
print('Theoretical Equations:')
for i in range(len(theoreticalA)):
    # round to 3 decimal places for printing
    formatted_theoretical_a = str(round(theoreticalA[i], 3))
    formatted_theoretical_c = str(round(theoreticalC[i], 3))
    # Replace A and C with the rounded values
    latex_formatted_equation = str(r'$V(t)=Ae^{-Ct}$').replace('A', formatted_theoretical_a).replace('C', formatted_theoretical_c)
    theoretical_equations.append(latex_formatted_equation) # add to list

# Get the rest of the data
capacitances = data['Capacitor Size'].tolist()
resistances = data['Resistance'].tolist()
logger_tau = data['Logger Tau'].tolist()
theoretical_tau = data['Theoretical Tau'].tolist()
percent_error = data['Percent Error'].tolist()

# Example output:
# 230000 \mu F & 99.7 \Omega & $V(t)=5.656e^{-0.0393t}+0.118$ & 25.432 s & $V(t)=5.828e^{-0.044t}$ & 22.931 s & 10.908\% \\

# Loop through all the data and print it in the correct format
for i in range(len(capacitances)):
    capacitance = str(capacitances[i])
    resistance = str(resistances[i])
    logger_equation = logger_equations[i]
    theoretical_equation = theoretical_equations[i]
    logger_tau_value = str(round(logger_tau[i], 3))
    theoretical_tau_value = str(round(theoretical_tau[i], 3))
    percent_error_value = str(round(percent_error[i], 3))
    print(f'${capacitance} \mu F$ & ${resistance} \Omega$ & {logger_equation} & {logger_tau_value} s & {theoretical_equation} & {theoretical_tau_value} s & {percent_error_value}\% \\\ ')