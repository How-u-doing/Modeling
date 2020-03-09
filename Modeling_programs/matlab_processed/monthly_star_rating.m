%load('hair_dryer.mat','hairdryer');
load('microwave.mat', 'microwave');
%load('pacifier.mat','pacifier');
%product_name = pacifier; product_str = 'Pacifier';
product_name = microwave; product_str = 'Microwave';
%product_name = hairdryer; product_str = 'Hairdryer';

monthNumber=(2015-2008+1)*12-4;
monthArray=product_name.review_date(1:monthNumber);
aveArray=zeros(monthNumber,1);
i = 1;
for y=2008: 2015
    iy=find(product_name.review_date.Year==y);
    if y==2015
        n_m=8;
    else
        n_m=12;
    end
    for m=1:n_m
        im=find(product_name.review_date.Month(iy)==m);
        s=sum(product_name.star_rating(iy(1)+im-1));
        n = length(im);
        if n>=1
            ave=s/n;
        else
            ave = 0;
        end
        monthArray(i)=datetime(y,m,15);
        aveArray(i)=ave;
        i = i + 1;
    end
end
figure
plot(monthArray,aveArray,'-r')
xlabel('Year, Month (y,m)')
ylabel('The reference value of Si')
title([product_str, ' 2008-2015'])
