close all
% question 1
r1=0.2; r2=0.3;
a1=0.001; a2=0.002;
x0=100; y0=50;
disp('Question 1 --> see figure 1 & 2')
exer8_q124_helper(a1,a2,r1,r2,x0,y0)

% question 2
x0=100; y0=200;
disp('Question 2 --> see figure 3 & 4')
exer8_q124_helper(a1,a2,r1,r2,x0,y0)

% question 3
disp('Question 3 --> see the dynamic graph, figure 5')
exer8_q3_helper() % dynamic graph, script file (click to run)

% question 4
r1=0.2; r2=0.3;
a1=0.001; a2=0.002;
x0=100; y0=50;
years=200;
disp('Question 4 --> see figure 6 & 7')
exer8_q124_helper(a1,a2,r1,r2,x0,y0,years)

