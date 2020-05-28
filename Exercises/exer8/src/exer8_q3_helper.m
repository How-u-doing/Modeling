% script file (void function) to solve question 3 
% of exercise 8 by drawing a dynamic graph
function exer8_q3_helper()
n=20; % draw n graphs
r1=0.2; r2=0.3;
x0=100; y0=200;
a1=linspace(0.001,0.004,n);
a2=(a1+0.003)./(a1+0.001).*a1; % give it some reasonable relationship as you like

years=50;
% years=100;
x=zeros(1,years+1); % # of rats in 50 years
y=zeros(1,years+1); % # of owls in 50 years
x(1)=x0; y(1)=y0; % initial conditions

figure
for i=1:n
    % let E=(alpha, beta) be the equilibrium point
    % let x_{k+1}=x_k, y{k+1}=y_k, then solve them
    alpha=round(r1/a1(i));
    beta=round(r2/a2(i));
    plot(alpha,beta,'m*',x(1),y(1),'m*')
    msg = sprintf('E(%d, %d)',alpha,beta);
    text(alpha-10, beta+20, msg);
    for k=1:years
        x(k+1)=(1+r1-a1(i)*y(k))*x(k);
        % in prictice terms, # Of rats & owls are non-negative
        if x(k+1)>0
            x(k+1)=round(x(k+1)); % # can only be integer, e.g. 4.3->4, 4.6->5
        else 
            x(k+1)=0;
        end
        
        y(k+1)=(1-r2+a2(i)*x(k))*y(k);
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
    msg = sprintf('Initial Point(%d, %d)', x(1),y(1));
    text(x(1)-20, y(1)+20, msg);
    hold on
    plot(x(years+1),y(years+1),'m*')
    msg = sprintf('End Point(%d, %d)', x(years+1),y(years+1));
    text(x(years+1)-20, y(years+1)+20, msg);
    xlabel('Rats #'), ylabel('Owls #')
    title_str=sprintf('# of Rats vs. Owls in %d years',years);
    title(title_str)
    
    hold off
    pause(1)
end

