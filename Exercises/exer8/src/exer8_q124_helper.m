% programs to solve question 1, 2, & 4 of exercise 8 in page 231
function exer8_q124_helper(a1,a2,r1,r2,x0,y0,years)
% set default args
if nargin<7
    years=50; % for question 1,2
    if nargin<6
        error('Too few arguments')
    end
end

time=0:years;
x=zeros(1,years+1); % # of rats in 50 years
y=zeros(1,years+1); % # of owls in 50 years
x(1)=x0; y(1)=y0; % initial conditions

figure
% let E=(alpha, beta) be the equilibrium point
% let x_{k+1}=x_k, y{k+1}=y_k, then solve them
alpha=round(r1/a1);
beta=round(r2/a2);
plot(alpha,beta,'m*',x(1),y(1),'m*')
msg = sprintf('E(%d, %d)',alpha,beta);
text(alpha-10, beta+20, msg);
for k=1:years
   x(k+1)=(1+r1-a1*y(k))*x(k);
    % in prictice terms, # Of rats & owls are non-negative
    if x(k+1)>0
        x(k+1)=round(x(k+1)); % # can only be integer, e.g. 4.3->4, 4.6->5
    else 
        x(k+1)=0;
    end

    y(k+1)=(1-r2+a2*x(k))*y(k);
    if y(k+1)>0
        y(k+1)=round(y(k+1));
    else 
        y(k+1)=0;
    end
    
    % draw vecters (with arrow) every two points
    
    hold on
    plot(x(k),y(k),'b.', x(k+1),y(k+1),'b.')
    vectarrow([x(k),y(k)],[x(k+1),y(k+1)])
end
% let E=(alpha, beta) be the equilibrium point
% let x_{k+1}=x_k, y{k+1}=y_k, then solve them
alpha=r1/a1;
beta=r2/a2;
hold on
plot(alpha,beta,'m*')
msg = sprintf('Initial Point(%d, %d)', x(1),y(1));
text(x(1)-20, y(1)+20, msg);

hold on
plot(x(years+1),y(years+1),'m*')
msg = sprintf('End Point(%d, %d)', x(years+1),y(years+1));
text(x(years+1)-20, y(years+1)+20, msg);
xlabel('Rats #'), ylabel('Owls #')
title_str=sprintf('# of Rats vs. Owls in %d years',years);
title(title_str)

figure
subplot(2,1,1)
plot(time,x,'-b.')
xlabel('Year'), ylabel('Rats #')
title_str=sprintf('Rats # in %d years',years);
title(title_str)

subplot(2,1,2)
plot(time,y,'-r.')
xlabel('Year'), ylabel('Owls #')
title_str=sprintf('Owls # in %d years',years);
title(title_str)
end

